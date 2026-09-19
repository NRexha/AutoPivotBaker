import bpy #pyright: ignore[reportMissingModuleSource]
from ..core import geometry_nodes

class APB_OT_load_geometry_nodes(bpy.types.Operator):
    bl_idname = "apb.load_geometry_nodes"
    bl_label = "Load Geometry Nodes"
    bl_description = "Load the APB Geometry Nodes into the current Blender file"
    def execute(self, context):
        loaded = geometry_nodes.load_geometry_nodes()
        if loaded:
            self.report({'INFO'}, "APB Geometry Nodes loaded")
        else:
            self.report({'INFO'}, "APB Geometry Nodes are already loaded")
        return {'FINISHED'}

class APB_OT_unload_geometry_nodes(bpy.types.Operator):
    bl_idname = "apb.unload_geometry_nodes"
    bl_label = "Unload Geometry Nodes"
    bl_description = "Remove unused APB Geometry Nodes from the current Blender file"
    def execute(self, context):
        unloaded = geometry_nodes.unload_geometry_nodes()
        if unloaded:
            self.report({'INFO'}, "APB Geometry Nodes unloaded")
        else:
            self.report({'INFO'}, "No unused APB Geometry Nodes to unload")
        return {'FINISHED'}