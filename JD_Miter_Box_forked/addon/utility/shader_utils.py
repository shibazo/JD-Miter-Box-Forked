import bpy


def get_builtin_shader_for_primitive(primitive_type):
    major, minor, patch = bpy.app.version

    if primitive_type == 'TRIS':
        return 'UNIFORM_COLOR'

    elif primitive_type == 'LINES':
        return 'POLYLINE_UNIFORM_COLOR'

    elif primitive_type == 'LINE_STRIP':
        return 'POLYLINE_UNIFORM_COLOR'

    elif primitive_type == 'POINTS':
        return 'UNIFORM_COLOR'

    else:
        return 'DEFAULT_SHADER'
    