import bpy  #pyright: ignore[reportMissingModuleSource]


class APB_PT_main(bpy.types.Panel):
    bl_label = "Auto Pivot Baker"
    bl_idname = "APB_PT_main"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pivot Baker"

    def draw(self, context):
        layout = self.layout
        settings = context.scene.apb_settings
        layout.label(text="Auto Pivot Baker")
        #collection
        layout.prop(settings, "collection")
        #target engine
        layout.prop(settings, "target_engine")
        #options
        layout.prop(settings, "store_random")
        layout.prop(settings, "store_forward")

        #bake
        layout.separator()
        layout.operator("apb.bake")