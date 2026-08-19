import bpy #pyright: ignore[reportMissingModuleSource]

from ..core.baker import bake_pivot

class APB_OT_bake(bpy.types.Operator):
    bl_idname = "apb.bake"
    bl_label = "Bake Pivot"

    def execute(self, context):
        bake_pivot()

        return {'FINISHED'}