import bpy #pyright: ignore[reportMissingModuleSource]

from ..core.geometry_nodes import load_geometry_nodes


class APB_OT_load_gn(bpy.types.Operator):

    bl_idname = "apb.load_gn"
    bl_label = "Load Geometry Nodes"

    def execute(self, context):

        load_geometry_nodes()

        return {'FINISHED'}