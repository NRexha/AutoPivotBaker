# Auto Pivot Baker

<div align="center">
<a href="https://github.com/NRexha/AutoPivotBaker/releases/">
  <img src="https://img.shields.io/github/release/NRexha/AutoPivotBaker?include_prereleases=&sort=semver&color=blue&label=Latest%20Release" alt="GitHub release"></a>
<a href="https://extensions.blender.org/add-ons/autopivotbaker/">
  <img src="https://img.shields.io/badge/Blender_Extensions-Install-orange" alt="Install from Blender Extensions"></a>
<a href="https://github.com/NRexha/AutoPivotBaker/blob/main/pyproject.toml">
  <img src="https://img.shields.io/badge/dynamic/toml?url=https%3A%2F%2Fraw.githubusercontent.com%2FNRexha%2FAutoPivotBaker%2Frefs%2Fheads%2Fmain%2Fpyproject.toml&query=project.requires-python&label=Python&logo=python&logoColor=white" alt="Required Python version"></a>
<a href="#license" title="Go to license section">
  <img src="https://img.shields.io/badge/License-GPL--3.0-blue" alt="License"></a>
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
<img width="1920" height="1009" alt="quick_demo" src="https://github.com/user-attachments/assets/64670194-bc1e-40f1-be03-3ebe4dcd7caf" />

### 1. Prepare the source meshes

Place the mesh objects you want to bake into a collection. Each object will be treated as an individual piece, and its pivot data will be stored in the resulting mesh. So be sure that each pivot is at the desired location.

### 2. Configure the bake settings

Open the *APB* panel in the 3D Viewport sidebar and configure the following options:

- **Collection:** Select the collection containing the source meshes.
- **Target Engine:** Choose Unreal Engine or Unity to apply the corresponding coordinate mapping.
- **Mesh Origin:** Choose the origin placement for the resulting combined mesh (this can either be changed manually after the baking).
- **Export FBX:** Check if you want to export the baked mesh as an FBX file.

### 3. Bake the mesh

Click **Bake Pivot** to generate the combined mesh with the pivot data stored in its UV channels. The original source collection is preserved. The resulting mesh is created separately and can then be exported to your target engine.

### 4. Use the baked data in your engine

Import the resulting mesh into your target engine and access the baked pivot data in your material or shader. The exact UV channels and coordinate mappings depend on the selected target engine. (In the sample projects, you can find a subgraph/material function that correctly extracts the pivot data).

## Geometry Nodes

The **Advanced** section provides access to the Geometry Nodes setup used by Auto Pivot Baker.

<img width="1920" height="1009" alt="load_gn" src="https://github.com/user-attachments/assets/888b279d-dd6b-49a9-afaf-83bc5e5df225" />

This workflow is intended for users who want to customize the baking process, store additional per-instance data in vertex colors, or modify the generated data before exporting.

Customizing this setup requires an understanding of Geometry Nodes and the target engine's mesh import and vertex attribute conventions. You are responsible for ensuring that custom data is exported and interpreted correctly by your target engine. Explanations on nodes and nodes inputs are available as tooltips, just hover them to know how they work.

**Note:** Geometry Nodes customization is optional. The standard baking workflow does not require any manual interaction with the node setup. I created the nodes in case you need a custom workflow, and in my opinion, nodes are easier to implement in an existing pipeline.

## Sample Projects

- Sample projects are available for both Unity and Unreal Engine. They demonstrate how to use meshes created with Auto Pivot Baker in materials and procedural animation workflows.
  <img width="1920" height="1080" alt="SampleScenes" src="https://github.com/user-attachments/assets/131535a4-da23-41b9-9d12-d70325abee75" />
  
- Each project has explanations on how to achieve the desired effect. The release also includes the Blender project used to create the meshes featured in these samples, allowing you to inspect the source meshes and their preparation.
  <img width="1920" height="1080" alt="Annotations" src="https://github.com/user-attachments/assets/a90727a3-f164-48fb-ac7b-11e9490ebe94" />

Those projects are also available here in the [releases page](../../releases).

## Supported Versions

- **Blender:** 5.0+
- **Unreal Engine:** 5.7+
- **Unity:** 6000.1+

## License

Released under <a href="/LICENSE">GPL-3.0</a> by <a href="https://github.com/NRexha">@NRexha</a>.
