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

        baked_object = baker.bake_pivot(settings.collection, settings.target_engine)

        if baked_object is None:
            return {'CANCELLED'}

        if settings.export_mesh:
            success = exporter.export_fbx(baked_object, settings.target_engine, settings.export_path)
            if not success:
                self.report({'ERROR'}, "Failed to export FBX.")
                return {'CANCELLED'}
        return {'FINISHED'}