ENGINE_SETTINGS = {

    "UNREAL": {
        "position_scale": 100.0,

        "pivot_mapping": (
            ("X", 1.0),
            ("Y", 1.0),
            ("Z", 1.0),
        ),

        "fbx_forward": "-Y",
        "fbx_up": "Z",

        "apply_unit_scale": True,
        "use_space_transform": True,
        "bake_space_transform": False,

        "export_rotation_x": 0,
    },

    "UNITY": {
        "position_scale": 1.0,

        "pivot_mapping": (
            ("X", -1.0),
            ("Z", 1.0),
            ("Y", -1.0),
        ),

        "fbx_forward": "-Z",
        "fbx_up": "Y",

        "apply_unit_scale": True,
        "use_space_transform": True,
        "bake_space_transform": True,

        "export_rotation_x": 90,
    }

}