import bpy  # pyright: ignore[reportMissingModuleSource]

def find_layer_collection(layer_collection, collection):
    if layer_collection.collection == collection:
        return layer_collection

    for child in layer_collection.children:
        result = find_layer_collection(child, collection)
        if result:
            return result
    return None

def get_baked_collection():
    collection = bpy.data.collections.get("APB Baked Meshes")
    if collection is None:
        collection = bpy.data.collections.new("APB Baked Meshes")
        bpy.context.scene.collection.children.link(collection)
    collection.color_tag = 'COLOR_01'
    return collection