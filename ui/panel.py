import bpy #pyright: ignore[reportMissingModuleSource]

class APB_PT_main(bpy.types.Panel):
    bl_label = "Auto Pivot Baker"
    bl_idname = "APB_PT_main"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pivot Baker"

    def draw(self, context):
        layout = self.layout
        layout.label(text="Auto Pivot Baker")
        layout.operator("apb.bake")