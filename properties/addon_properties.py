import bpy #pyright: ignore[reportMissingModuleSource]

class APB_PG_settings(bpy.types.PropertyGroup):

    collection: bpy.props.PointerProperty(
        name="Collection",
        description="Collection contaning the separate objects to bake",
        type=bpy.types.Collection
    )#pyright: ignore[reportInvalidTypeForm]

    target_engine: bpy.props.EnumProperty(
        name="Target Engine",
        description="Target game engine for the baked data",
        items=[
            ('UNREAL', "Unreal", "Bake data for Unreal Engine"),
            ('UNITY', "Unity", "Bake data for Unity"),
        ],
        default='UNREAL'
    )#pyright: ignore[reportInvalidTypeForm]

    export_mesh: bpy.props.BoolProperty(
        name="Export Mesh",
        description="Export the baked mesh as an FBX. Export settings are based on the selected target engine.",
        default=False
    )#pyright: ignore[reportInvalidTypeForm]

    export_path: bpy.props.StringProperty(
        name="Export Folder",
        description="Folder where the baked FBX will be exported",
        subtype='DIR_PATH'
    )#pyright: ignore[reportInvalidTypeForm]


def register():
    bpy.types.Scene.apb_settings = bpy.props.PointerProperty(type=APB_PG_settings)


def unregister():
    del bpy.types.Scene.apb_settings