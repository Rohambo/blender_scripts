
import bpy
import bmesh

'''
Toggles the show_viewport of subdiv modifier on selected object/s based on the value of the last selected object.
If a mesh has multiple subdiv modifiers, it operates on the last one tree.
If the last selected object doesn't have a subdiv modifier, the tool will skip the toggle.
'''

def toggleSubdiv():
    objs = bpy.context.selected_objects
    activeObj = bpy.context.active_object
    activeObjSubDiv = None
    activeObjMod = activeObj.modifiers
    selectedObjMod = None
    toggleVal = False
    
    if not activeObjMod:
        print ("No modifiers on last selected object!")
        return
    
    for md in activeObjMod:
        if md.type == "SUBSURF":
            activeObjSubDiv = md
    
    if not activeObjSubDiv:
        print ("No subdiv modifiers found on last selected object!")
        return
    
    toggleVal = not activeObjSubDiv.show_viewport
    
    for ob in objs:
        if not ob.modifiers:
            continue
        for md in ob.modifiers:
            if md.type == "SUBSURF":
                selectedObjMod = md
        selectedObjMod.show_viewport = toggleVal
        
    
try:        
    toggleSubdiv()
except Exception as e:
    print ("Failed to toggle!\nError: %s"%e)
    
