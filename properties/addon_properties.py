import bpy #pyright: ignore[reportMissingModuleSource]


class APB_PG_settings(bpy.types.PropertyGroup):

    collection: bpy.props.PointerProperty(
        name="Collection",
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

    store_random: bpy.props.BoolProperty(
        name="Store Random",
        description="Store a random value with the pivot data",
        default=False
    )#pyright: ignore[reportInvalidTypeForm]

    store_forward: bpy.props.BoolProperty(
        name="Store Forward",
        description="Store the instance forward vector",
        default=False
    )#pyright: ignore[reportInvalidTypeForm]


def register():
    bpy.types.Scene.apb_settings = bpy.props.PointerProperty(
        type=APB_PG_settings
    )


def unregister():
    del bpy.types.Scene.apb_settings