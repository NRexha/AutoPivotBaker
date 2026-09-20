import bpy  # pyright: ignore[reportMissingModuleSource]
import math
from pathlib import Path

from .engine_settings import ENGINE_SETTINGS


def export_fbx(baked_object, target_engine, export_path):
    engine = ENGINE_SETTINGS.get(target_engine)
    if engine is None:
        #print(f"Unsupported target engine: {target_engine}")
        return False

    if baked_object is None:
        #print("No baked object to export.")
        return False

    if not export_path:
        #print("No export folder specified.")
        return False

    export_folder = Path(bpy.path.abspath(export_path))
    export_folder.mkdir(parents=True, exist_ok=True)
    filename = f"{baked_object.name}.fbx"
    filepath = export_folder/filename
    bpy.ops.object.select_all(action='DESELECT')
    baked_object.select_set(True)
    bpy.context.view_layer.objects.active = baked_object

    original_rotation = baked_object.rotation_euler.copy()
    rotation_x = engine.get("export_rotation_x", 0)
    if rotation_x != 0:
        baked_object.rotation_euler.x += math.radians(rotation_x)
    try:
        bpy.ops.export_scene.fbx(
            filepath=str(filepath),
            use_selection=True,
            use_mesh_modifiers=True,
            axis_forward=engine["fbx_forward"],
            axis_up=engine["fbx_up"],
            object_types={'MESH'},
            use_custom_props=False,
            apply_unit_scale=engine.get("apply_unit_scale", False),
            use_space_transform=engine.get("use_space_transform", True),
            bake_space_transform=engine.get("bake_space_transform", False),
        )

    finally:
        baked_object.rotation_euler = original_rotation
    #print(f"Exported: {filepath}")
    return True