import bpy
import bmesh

def toggleBevel():

    obj = bpy.context.object
    mesh = obj.data
    bm = bmesh.from_edit_mesh(mesh)

    bevelWeightLayer = bm.edges.layers.bevel_weight['BevelWeight']
    selectedEdges = [e for e  in bm.edges if e.select]
    lastEdge = selectedEdges[-1]

    value = not bool(lastEdge[bevelWeightLayer])

    for edge in selectedEdges:
        edge[bevelWeightLayer] = value

    bmesh.update_edit_mesh(mesh)

try:
    toggleBevel()
except Exception as e:
    print ("Failed to toggle!\nError: %s"%e)

