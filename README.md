# Auto Pivot Baker

<div align="center">
  <a href="https://github.com/NRexha/AutoPivotBaker/releases/">
    <img src="https://img.shields.io/github/release/NRexha/AutoPivotBaker?include_prereleases=&sort=semver&color=blue&label=Latest%20Release&style=flat-square" alt="GitHub release"></a>
  <a href="https://extensions.blender.org/add-ons/autopivotbaker/">
    <img src="https://img.shields.io/badge/Blender_Extensions-Install-orange?style=flat-square" alt="Install from Blender Extensions"></a>
  <a href="https://github.com/NRexha/AutoPivotBaker/blob/main/pyproject.toml">
    <img src="https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FNRexha%2FAutoPivotBaker%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=project.requires-python&label=Python&logo=python&logoColor=white&style=flat-square" alt="Required Python version"></a>
  <a href="#license" title="Go to license section">
    <img src="https://img.shields.io/badge/License-GPL--3.0-blue?style=flat-square" alt="License"></a>
</div>
<br>

Auto Pivot Baker is a Blender extension that bakes per-object pivot data into UV channels, allowing multiple mesh objects to be combined into a single mesh while preserving their individual pivots. 

The baked data can drive procedural mesh animation and vertex displacement through materials and shaders in Unreal Engine and Unity, without requiring each piece to remain a separate mesh object.

<img width="825" height="328" alt="image" src="https://github.com/user-attachments/assets/6d3e8382-c6b8-45d5-bbd4-636f492b3905" />

## Installation

Auto Pivot Baker can either be installed from [*Blender Extensions* website](https://extensions.blender.org/add-ons/autopivotbaker/) or from the [releases page](../../releases). You can either just simply drag & drop the zip file in Blender or use the *Install from Disk* method.

## Features

- Bake pivot data from mesh objects contained in a collection.
- Support for **Unreal Engine** and **Unity** (handles correct scale, axis mapping etc...).
- Store per-object random values.
- Optionally store custom vector data in vertex colors.

## Usage
1. Place your source meshes in a collection and set each object's pivot where you want it.

2. Open the APB panel in the 3D Viewport sidebar. Select the collection, target engine, mesh origin, and optional FBX export.

3. Click *Bake Pivot* to create a combined mesh with the pivot data stored in its UV channels. Your original source collection is preserved.

4. Import the mesh into your engine and access the baked data through your material or shader. The sample projects include material functions and subgraphs for reading the data.
<img width="1920" height="1009" alt="quick_demo" src="https://github.com/user-attachments/assets/64670194-bc1e-40f1-be03-3ebe4dcd7caf" />

## Geometry Nodes

The optional Advanced section exposes the Geometry Nodes setup for customizing the baking process, storing additional per-instance data, or modifying the generated attributes. Tooltips explain the nodes and their inputs. The standard workflow does not require any manual interaction with Geometry Nodes. They are named *APB_PreparePivotData* and *APB_StorePivotData*.

<img width="1920" height="1009" alt="load_gn" src="https://github.com/user-attachments/assets/888b279d-dd6b-49a9-afaf-83bc5e5df225" />

## Sample Projects

Sample projects are available for both Unity and Unreal Engine. They demonstrate how to use meshes created with Auto Pivot Baker in materials and procedural animation workflows. Each project has explanations on how to achieve the desired effect. The release also includes the Blender project used to create the meshes featured in these samples, allowing you to inspect the source meshes and their preparation. Those projects are also available here in the [releases page](../../releases).

<img width="1920" height="1080" alt="SampleScenes" src="https://github.com/user-attachments/assets/131535a4-da23-41b9-9d12-d70325abee75" />
  
## Supported Versions

- **Blender:** 5.0+
- **Unreal Engine:** 5.7+
- **Unity:** 6000.1+

## License

Released under <a href="/LICENSE">GPL-3.0</a> by <a href="https://github.com/NRexha">@NRexha</a>.
