import bpy #pyright: ignore[reportMissingModuleSource]

from .properties.addon_properties import APB_PG_settings
from .operators.op_baker import APB_OT_bake
from .operators.op_gn_handler import (APB_OT_load_geometry_nodes, APB_OT_unload_geometry_nodes,)
from .ui.panel import APB_PT_main


classes = (
    APB_PG_settings,
    APB_OT_bake,
    APB_OT_load_geometry_nodes,
    APB_OT_unload_geometry_nodes,
    APB_PT_main,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.apb_settings = bpy.props.PointerProperty(type=APB_PG_settings)


def unregister():
    del bpy.types.Scene.apb_settings

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
