import bpy

def get_builtin_shader():
    major, minor, patch = bpy.app.version

    if (major, minor) == (3, 3):
        return '3D_UNIFORM_COLOR'
    elif (major, minor) >= (3, 4):
        return 'UNIFORM_COLOR'
    elif (major, minor) >= (4, 0) and  (major, minor) < (4, 5):
        return 'UNIFORM_COLOR'
    elif (major, minor) >= (4, 5):
        return 'POLYLINE_UNIFORM_COLOR'
    else:
        return 'DEFAULT_SHADER'  # フォールバック

def get_builtin_shader_2d():
    major, minor, patch = bpy.app.version

    if (major, minor) == (3, 3):
        return '2D_UNIFORM_COLOR'
    elif (major, minor) >= (3, 4):
        return 'UNIFORM_COLOR'
    elif (major, minor) >= (4, 0) and  (major, minor) < (4, 5):
        return 'UNIFORM_COLOR'
    elif (major, minor) >= (4, 5):
        return 'POLYLINE_UNIFORM_COLOR'
    else:
        return 'DEFAULT_SHADER'  # フォールバック
