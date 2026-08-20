import bpy #pyright: ignore[reportMissingModuleSource]
from .core import geometry_nodes

class APB_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__
    add_geometry_nodes: bpy.props.BoolProperty(
        name="Add APB Geometry Nodes",
        description="Add the APB Geometry Nodes to this Blender file",
        default=False,
        update=lambda self, context: geometry_nodes.update_geometry_nodes(self, context)
    )#pyright: ignore[reportInvalidTypeForm]

    def draw(self, context):
        layout = self.layout
        layout.operator("wm.url_open", text="Documentation", icon='HELP').url = "https://github.com/NRexha"
        layout.prop(self, "add_geometry_nodes") #temporary
        layout.label(text="Auto Pivot Baker")