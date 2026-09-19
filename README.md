# Auto Pivot Baker

Auto Pivot Baker is a Blender extension for baking per-instance pivot data from separate mesh objects into UV channels, making it easy to use that data for procedural mesh animation and vertex offset workflows in game engines.

## Features

* Bake pivot data from a collection of mesh objects
* Support for **Unreal Engine** and **Unity**
* Store per-instance random values
* Can also store custom vectors in vertex color.
* Keep original mesh UVs

## Usage

1. Add the mesh objects you want to bake to a collection.
2. Open the **Pivot Baker** tab in the 3D Viewport sidebar.
3. Select your collection.
4. Select the target engine.
5. Choose the desired mesh origin.
6. Optionally export the resulting mesh as an FBX.
7. Click **Bake**.

The baked pivot data is stored in UV channels so it can be accessed in the target engine's material or shader.

## Advanced Geometry Nodes

The **Advanced** section allows experienced users to load the Geometry Nodes used by Auto Pivot Baker. This can be used to create custom workflows, store additional per-instance data, or modify the baked data before exporting. However this means that you need to know how to correctly export meshes and data for you target game engine.

The Geometry Nodes are optional and are not required for the standard baking workflow.

## Supported Versions

* Blender 5.0+
* Unreal Engine
* Unity

## Installation

### Blender Extensions

Auto Pivot Baker can be either installed through the Blender Extensions platform or from the [releases page](../../releases).

## License

See [LICENSE](LICENSE) for license information.
