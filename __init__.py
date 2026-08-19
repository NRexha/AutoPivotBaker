bl_info = {
    "name": "Auto Pivot Baker",
    "author": "NRexha",
    "description": "",
    "blender": (5, 00, 0),
    "version": (0, 0, 1),
    "location": "",
    "warning": "",
    "category": "Generic",
}

from . import auto_load

auto_load.init()


def register():
    auto_load.register()


def unregister():
    auto_load.unregister()
