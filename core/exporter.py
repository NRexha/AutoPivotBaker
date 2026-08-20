import bpy #pyright: ignore[reportMissingModuleSource]
from pathlib import Path
from .engine_settings import ENGINE_SETTINGS


def export_fbx(baked_object, target_engine, export_path):

    engine = ENGINE_SETTINGS.get(target_engine)

    if engine is None:
        print(f"Unsupported target engine: {target_engine}")
        return False

    if baked_object is None:
        print("No baked object to export.")
        return False

    if not export_path:
        print("No export folder specified.")
        return False

    #get export folder
    export_folder = Path(bpy.path.abspath(export_path))
    export_folder.mkdir(parents=True, exist_ok=True)
    filename = f"{baked_object.name}.fbx"
    filepath = export_folder / filename
    bpy.ops.object.select_all(action='DESELECT')
    baked_object.select_set(True)
    bpy.context.view_layer.objects.active = baked_object

    bpy.ops.export_scene.fbx(
        filepath=str(filepath),
        use_selection=True,
        use_mesh_modifiers=True,
        axis_forward=engine["fbx_forward"],
        axis_up=engine["fbx_up"],
        object_types={'MESH'},
        use_custom_props=False,
    )

    print(f"Exported: {filepath}")

    return True