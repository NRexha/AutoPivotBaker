import bpy #pyright: ignore[reportMissingModuleSource]

class APB_PT_main(bpy.types.Panel):
    bl_label = "Auto Pivot Baker"
    bl_idname = "APB_PT_main"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Pivot Baker"

    def draw(self, context):
        layout = self.layout
        settings = context.scene.apb_settings
        #settings section
        layout.label(text="Baking Settings")
        layout.prop(settings, "collection")
        layout.prop(settings, "target_engine")
        layout.prop(settings, "mesh_origin")
        layout.separator()
        layout.prop(settings, "export_mesh")
        if settings.export_mesh:
            layout.prop(settings, "export_path")
        layout.separator()
        layout.operator("apb.bake")
        layout.separator()
        #advanced section
        header, body = layout.panel("APB_PT_geometry_nodes", default_closed=True)
        header.label(text="Advanced")
        if body:
            body.operator("apb.load_geometry_nodes", text="Load APB Geometry Nodes", icon='IMPORT')
            body.operator("apb.unload_geometry_nodes", text="Unload APB Geometry Nodes", icon='X')