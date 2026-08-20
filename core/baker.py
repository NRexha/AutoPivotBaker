import bpy #pyright: ignore[reportMissingModuleSource]
import random
from .engine_settings import ENGINE_SETTINGS

def bake_pivot(collection, target_engine):

    #get engine settings
    engine = ENGINE_SETTINGS.get(target_engine)

    if engine is None:
        print(f"Unsupported target engine: {target_engine}")
        return None

    #gather obj
    source_objects = [obj for obj in collection.objects if obj.type == 'MESH']

    if not source_objects:
        print("No mesh objects found.")
        return None

    duplicated_objects = []

    #store pivot pos and random value (k=duplicated obj, v=ws pos/random)
    pivot_data = {}
    random_data = {}

    for source_obj in source_objects:
        new_obj = source_obj.copy()
        new_obj.data = source_obj.data.copy() #keep original mesh data
        bpy.context.scene.collection.objects.link(new_obj)
        duplicated_objects.append(new_obj)
        pivot_data[new_obj] = source_obj.matrix_world.translation.copy()
        random_data[new_obj] = random.random()

    #prepare obj
    bpy.ops.object.select_all(action='DESELECT')
    for obj in duplicated_objects:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = duplicated_objects[0]
    bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)

    #store pivot position as temporary attribute
    temp_attribute_name = "APB_TEMP_Pivot"
    temp_random_name = "APB_TEMP_Random"

    for obj in duplicated_objects:
        mesh = obj.data
        pivot_attribute = mesh.attributes.new(name=temp_attribute_name, type='FLOAT_VECTOR', domain='POINT')
        random_attribute = mesh.attributes.new(name=temp_random_name, type='FLOAT', domain='POINT')
        pivot = pivot_data[obj]
        pivot *= engine["position_scale"]
        random_value = random_data.get(obj, 0.0)
        for vertex in mesh.vertices:
            pivot_attribute.data[vertex.index].vector = pivot
            random_attribute.data[vertex.index].value = random_value

    #join obj
    bpy.context.view_layer.objects.active = duplicated_objects[0]
    bpy.ops.object.join()
    combined_object = bpy.context.object
    #set origin to geometry
    bpy.ops.object.origin_set(type='ORIGIN_GEOMETRY', center='MEDIAN')

    #create UV attributes
    mesh = combined_object.data
    uv_xy = mesh.uv_layers.get("APB_PivotXY")
    if uv_xy is None:
        uv_xy = mesh.uv_layers.new(name="APB_PivotXY")
    uv_zrand = mesh.uv_layers.get("APB_PivotZRand")
    if uv_zrand is None:
        uv_zrand = mesh.uv_layers.new(name="APB_PivotZRand")

    #write pivot data
    pivot_attribute = mesh.attributes.get(temp_attribute_name)
    random_attribute = mesh.attributes.get(temp_random_name)

    for loop in mesh.loops:
        pivot = pivot_attribute.data[loop.vertex_index].vector
        random_value = random_attribute.data[loop.vertex_index].value
        pivot = combined_object.matrix_world.inverted() @ pivot
        uv_xy.data[loop.index].uv = (pivot.x, pivot.y)

        #store engine-specific pivot axis
        match(engine["pivot_axis"]):
            case "Z":
                pivot_axis = pivot.z
            case "Y":
                pivot_axis = pivot.y
            case "X":
                pivot_axis = pivot.x
        uv_zrand.data[loop.index].uv = (pivot_axis, random_value)

    #cleanup at end
    mesh.attributes.remove(pivot_attribute)
    mesh.attributes.remove(random_attribute)
    bpy.context.view_layer.layer_collection.children[collection.name].exclude = True
    combined_object.name = f"{collection.name}_Baked"
    print("Created:", combined_object.name)
    
    return combined_object