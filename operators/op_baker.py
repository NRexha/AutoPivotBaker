import bpy  #pyright: ignore[reportMissingModuleSource]

from ..core.baker import bake_pivot

class APB_OT_bake(bpy.types.Operator):
    bl_idname = "apb.bake"
    bl_label = "Bake Pivot"

    def execute(self, context):
        settings = context.scene.apb_settings
        if settings.collection is None:
            self.report(
                {'WARNING'},
                "No collection selected"
            )
            return {'CANCELLED'}

        bake_pivot(settings.collection, settings.target_engine, settings.store_random, settings.store_forward)

        return {'FINISHED'}