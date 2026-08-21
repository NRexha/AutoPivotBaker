import bpy #pyright: ignore[reportMissingModuleSource]
from ..core import geometry_nodes

class APB_OT_load_geometry_nodes(bpy.types.Operator):
    bl_idname = "apb.load_geometry_nodes"
    bl_label = "Load Geometry Nodes"
    bl_description = "Load the APB Geometry Nodes into the current Blender file"
    def execute(self, context):
        geometry_nodes.load_geometry_nodes()
        return {'FINISHED'}

class APB_OT_unload_geometry_nodes(bpy.types.Operator):
    bl_idname = "apb.unload_geometry_nodes"
    bl_label = "Unload Geometry Nodes"
    bl_description = "Remove unused APB Geometry Nodes from the current Blender file"
    def execute(self, context):
        geometry_nodes.unload_geometry_nodes()
        return {'FINISHED'}