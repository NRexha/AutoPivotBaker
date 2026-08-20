import bpy #pyright: ignore[reportMissingModuleSource]
from pathlib import Path

GEOMETRY_NODES = ["APB_PreparePivotData", "APB_StorePivotData"]

def load_geometry_nodes():
    addon_path = Path(__file__).parent.parent
    file_path = addon_path/"assets"/"geometry_nodes.blend"

    for node_group_name in GEOMETRY_NODES:
        if node_group_name in bpy.data.node_groups:
            continue
        bpy.ops.wm.append(
            filepath=str(file_path / "NodeTree" / node_group_name),
            directory=str(file_path / "NodeTree"),
            filename=node_group_name
        )

def unload_geometry_nodes():
    for node_group_name in GEOMETRY_NODES:
        node_group = bpy.data.node_groups.get(node_group_name)
        if node_group is None:
            continue
        if node_group.users == 0:
            bpy.data.node_groups.remove(node_group)


def update_geometry_nodes(self, context):
    if self.add_geometry_nodes:
        load_geometry_nodes()
    else:
        unload_geometry_nodes()