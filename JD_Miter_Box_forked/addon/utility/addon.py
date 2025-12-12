import bpy

addon_name = None

def get_prefs():
    return bpy.context.preferences.addons[addon_name].preferences