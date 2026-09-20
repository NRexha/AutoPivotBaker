import bpy  # pyright: ignore[reportMissingModuleSource]
import random
from .engine_settings import ENGINE_SETTINGS
from . import utils

def get_pivot_component(pivot, mapping):
    axis, sign = mapping
    match axis:
        case "X":
            value = pivot.x
        case "Y":
            value = pivot.y
        case "Z":
            value = pivot.z
        case _:
            raise ValueError(f"Invalid pivot axis: {axis}")
    return value * sign

def set_mesh_origin(combined_object, mesh_origin):
    mesh = combined_object.data
    
    min_x = min(vertex.co.x for vertex in mesh.vertices)
    max_x = max(vertex.co.x for vertex in mesh.vertices)
    min_y = min(vertex.co.y for vertex in mesh.vertices)
    max_y = max(vertex.co.y for vertex in mesh.vertices)
    min_z = min(vertex.co.z for vertex in mesh.vertices)
    max_z = max(vertex.co.z for vertex in mesh.vertices)
    center_x = (min_x + max_x) * 0.5
    center_y = (min_y + max_y) * 0.5
    center_z = (min_z + max_z) * 0.5

    match mesh_origin:
        case "CENTER":
            origin_x = center_x
            origin_y = center_y
            origin_z = center_z
        case "BOTTOM_CENTER":
            origin_x = center_x
            origin_y = center_y
            origin_z = min_z
        case "TOP_CENTER":
            origin_x = center_x
            origin_y = center_y
            origin_z = max_z
        case _:
            raise ValueError(f"Invalid mesh origin: {mesh_origin}")

    for vertex in mesh.vertices:
        vertex.co.x -= origin_x
        vertex.co.y -= origin_y
        vertex.co.z -= origin_z
    combined_object.location.x += origin_x
    combined_object.location.y += origin_y
    combined_object.location.z += origin_z

def bake_pivot(collection, target_engine, mesh_origin):
    engine = ENGINE_SETTINGS.get(target_engine)
    if engine is None:
        #print(f"Unsupported target engine: {target_engine}")
        return None

    position_scale = engine["position_scale"]
    pivot_mapping = engine["pivot_mapping"]
    source_objects = [obj for obj in collection.objects if obj.type == 'MESH']

    if not source_objects:
        #print("No mesh objects found.")
        return None

    duplicated_objects = []
    pivot_data = {}
    random_data = {}

    for source_obj in source_objects:
        new_obj = source_obj.copy()
        new_obj.data = source_obj.data.copy()
        bpy.context.scene.collection.objects.link(new_obj)
        duplicated_objects.append(new_obj)
        pivot_data[new_obj] = source_obj.matrix_world.translation.copy()
        random_data[new_obj] = random.random()

    bpy.ops.object.select_all(action='DESELECT')
    for obj in duplicated_objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = duplicated_objects[0]
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

    temp_attribute_name = "APB_TEMP_Pivot"
    temp_random_name = "APB_TEMP_Random"

    for obj in duplicated_objects:
        mesh = obj.data
        pivot_attribute = mesh.attributes.new(name=temp_attribute_name, type='FLOAT_VECTOR', domain='POINT')
        random_attribute = mesh.attributes.new(name=temp_random_name, type='FLOAT', domain='POINT')
        pivot = pivot_data[obj].copy()
        pivot *= position_scale
        random_value = random_data.get(obj, 0.0)
        for vertex in mesh.vertices:
            pivot_attribute.data[vertex.index].vector = pivot
            random_attribute.data[vertex.index].value = random_value

    bpy.context.view_layer.objects.active = duplicated_objects[0]
    bpy.ops.object.join()
    combined_object = bpy.context.object
    set_mesh_origin(combined_object, mesh_origin)
    combined_object.location = (0.0, 0.0, 0.0)
    mesh = combined_object.data

    uv_xy = mesh.uv_layers.get("APB_PivotXY")
    if uv_xy is None:
        uv_xy = mesh.uv_layers.new(name="APB_PivotXY")

    uv_zrand = mesh.uv_layers.get("APB_PivotZRand")
    if uv_zrand is None:
        uv_zrand = mesh.uv_layers.new(name="APB_PivotZRand")

    pivot_attribute = mesh.attributes.get(temp_attribute_name)
    random_attribute = mesh.attributes.get(temp_random_name)

    if pivot_attribute is None:
        #print("Pivot attribute was not found.")
        return None

    if random_attribute is None:
        #print("Random attribute was not found.")
        return None

    for loop in mesh.loops:
        pivot = pivot_attribute.data[loop.vertex_index].vector.copy()
        random_value = random_attribute.data[loop.vertex_index].value
        pivot = combined_object.matrix_world.inverted() @ pivot
        uv_x = get_pivot_component(pivot, pivot_mapping[0])
        uv_y = get_pivot_component(pivot, pivot_mapping[1])
        uv_z = get_pivot_component(pivot, pivot_mapping[2])

        uv_xy.data[loop.index].uv = (uv_x, uv_y)
        uv_zrand.data[loop.index].uv = (uv_z, random_value)

    mesh.attributes.remove(pivot_attribute)
    mesh.attributes.remove(random_attribute)

    layer_collection = utils.find_layer_collection(bpy.context.view_layer.layer_collection, collection)

    if layer_collection:
        layer_collection.exclude = True
    combined_object.name = f"{collection.name}_Baked"

    baked_collection = utils.get_baked_collection()

    for object_collection in list(combined_object.users_collection):
        object_collection.objects.unlink(combined_object)
        
    baked_collection.objects.link(combined_object)

    #print(f"Created: {combined_object.name}")
    return combined_object