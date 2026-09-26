import bpy #pyright: ignore[reportMissingModuleSource]
from ..core import baker, exporter

class APB_OT_bake(bpy.types.Operator):
    bl_idname = "apb.bake"
    bl_label = "Bake Pivot"
    bl_description = "Bake pivot data"

    def execute(self, context):
        settings = context.scene.apb_settings

        if settings.collection is None:
            self.report({'ERROR'}, "No collection selected.")
            return {'CANCELLED'}
        
        if not any(obj.type == 'MESH' for obj in settings.collection.objects):
            self.report({'ERROR'}, "The selected collection contains no mesh objects.")
            return {'CANCELLED'}

        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')

        baked_object = baker.bake_pivot(settings.collection, settings.target_engine, settings.mesh_origin)

        if baked_object is None:
            self.report({'ERROR'}, "Failed to bake pivot data.")
            return {'CANCELLED'}

        if settings.export_mesh:
            success = exporter.export_fbx(baked_object, settings.target_engine, settings.export_path)
            if not success:
                self.report({'ERROR'}, "Failed to export FBX.")
                return {'CANCELLED'}
            self.report({'INFO'}, f"Baked and exported: {baked_object.name}")
        else:
            self.report({'INFO'}, f"Baked: {baked_object.name}")
        return {'FINISHED'}