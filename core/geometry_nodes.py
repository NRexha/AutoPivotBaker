import bpy #pyright: ignore[reportMissingModuleSource]
from pathlib import Path


GEOMETRY_NODES = [
    "APB_PreparePivotData",
    "APB_StorePivotData",
]


def load_geometry_nodes():
    addon_path = Path(__file__).parent.parent
    file_path = addon_path / "assets" / "geometry_nodes.blend"
    for node_group_name in GEOMETRY_NODES:
        if node_group_name in bpy.data.node_groups:
            continue
        bpy.ops.wm.append(
            filepath=str(file_path / "NodeTree" / node_group_name),
            directory=str(file_path / "NodeTree"),
            filename=node_group_name
        )
    print("Loaded APB Geometry Nodes.")