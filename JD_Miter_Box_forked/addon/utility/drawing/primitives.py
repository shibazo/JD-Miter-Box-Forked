import bpy
import gpu
from gpu_extras.batch import batch_for_shader
from mathutils import Vector

from ..math import rotate_to_space, rotate_point_around_axis
from ..shader_utils import get_builtin_shader_for_primitive


def plane_center(location, axis_x, axis_y, axis_z, size_x, size_y, color):
    size_x = size_x/2
    size_y = size_y/2

    positions = (
        Vector((-size_x,  size_y, 0)), Vector((size_x,  size_y, 0)),
        Vector((-size_x, -size_y, 0)), Vector((size_x, -size_y, 0))
        )

    indices = ((0, 1, 2), (2, 1, 3))

    positions = rotate_to_space(positions, axis_x, axis_y, axis_z)

    for vec in positions:
        vec += location

    gpu.state.blend_set('ALPHA')

    shader = gpu.shader.from_builtin(get_builtin_shader_for_primitive('TRIS'))
    batch = batch_for_shader(shader, 'TRIS', {"pos": positions}, indices=indices)

    shader.bind()
    shader.uniform_float("color", color)
    batch.draw(shader)

    gpu.state.blend_set('NONE')

def line(location, axis_x, axis_y, axis_z, length, thickness, color):
    world_coors = [Vector((0, 0, 0)), Vector((0, 0, length))]
    world_coors = rotate_to_space(world_coors, axis_x, axis_y, axis_z)
    for vec in world_coors:
        vec += location

    shader_moving_lines = gpu.shader.from_builtin(get_builtin_shader_for_primitive('LINES'))
    batch_moving_lines = batch_for_shader(shader_moving_lines, 'LINES', {"pos": world_coors})

    region = bpy.context.region
    viewport_size = (region.width, region.height)

    shader_moving_lines.bind()
    shader_moving_lines.uniform_float("color", color)
    shader_moving_lines.uniform_float("lineWidth", thickness)
    shader_moving_lines.uniform_float("viewportSize", viewport_size)
    batch_moving_lines.draw(shader_moving_lines)

def line_p2p(start, end, thickness, color):
    coors = [start, end]

    shader_line = gpu.shader.from_builtin(get_builtin_shader_for_primitive('LINES'))
    batch_line = batch_for_shader(shader_line, 'LINES', {"pos": coors})

    region = bpy.context.region
    viewport_size = (region.width, region.height)

    shader_line.bind()
    shader_line.uniform_float("color", color)
    shader_line.uniform_float("lineWidth", thickness)
    shader_line.uniform_float("viewportSize", viewport_size)

    batch_line.draw(shader_line)

def lines_p2p(coor_pairs, thickness, color):
    shader_line = gpu.shader.from_builtin(get_builtin_shader_for_primitive('LINES'))
    batch_line = batch_for_shader(shader_line, 'LINES', {"pos": coor_pairs})

    region = bpy.context.region
    viewport_size = (region.width, region.height)

    shader_line.bind()
    shader_line.uniform_float("color", color)
    shader_line.uniform_float("lineWidth", thickness)
    shader_line.uniform_float("viewportSize", viewport_size)
    batch_line.draw(shader_line)

def line_2d(start, end, thickness, color):
    world_coors = [start, end]

    shader_line = gpu.shader.from_builtin(get_builtin_shader_for_primitive('LINES'))
    batch_line = batch_for_shader(shader_line, 'LINES', {"pos": world_coors})

    region = bpy.context.region
    viewport_size = (region.width, region.height)

    shader_line.bind()
    shader_line.uniform_float("color", color)
    shader_line.uniform_float("lineWidth", thickness)
    shader_line.uniform_float("viewportSize", viewport_size)
    batch_line.draw(shader_line)

def edges(locations, thickness, color):
    shader_moving_lines = gpu.shader.from_builtin(get_builtin_shader_for_primitive('LINES'))
    batch_moving_lines = batch_for_shader(shader_moving_lines, 'LINES', {"pos": locations})

    region = bpy.context.region
    viewport_size = (region.width, region.height)

    shader_moving_lines.bind()
    shader_moving_lines.uniform_float("color", color)
    shader_moving_lines.uniform_float("lineWidth", thickness)
    shader_moving_lines.uniform_float("viewportSize", viewport_size)
    batch_moving_lines.draw(shader_moving_lines)

def points(locations, size, color):
    gpu.state.point_size_set(size)

    version = bpy.app.version
    shader_dots = gpu.shader.from_builtin(get_builtin_shader_for_primitive('POINTS'))
    if version >= (4, 5, 0):
        shader_dots = gpu.shader.from_builtin('POINT_UNIFORM_COLOR')

    batch_dots = batch_for_shader(shader_dots, 'POINTS', {"pos": locations})

    shader_dots.bind()
    shader_dots.uniform_float("color", color)
    batch_dots.draw(shader_dots)

    gpu.state.point_size_set(1)

def arc(center, axis_x, axis_y, axis_z, radius, angle, thickness, color):
    world_coors = []

    # every 5 degrees, we need angle/5 points
    angle_pts = abs(int(angle/5))
    if angle_pts != 0:
        angle_div = angle/angle_pts
    else:
        angle_div = 0

    for i in range(int(angle_pts)+1):
        point = rotate_point_around_axis(Vector((1,0,0)), Vector((0, radius, 0)), angle_div*i)
        world_coors.append(point)

    world_coors = rotate_to_space(world_coors, axis_x, axis_y, axis_z)

    for vec in world_coors:
        vec += center

    shader_arc = gpu.shader.from_builtin(get_builtin_shader_for_primitive('LINE_STRIP'))
    batch_arc = batch_for_shader(shader_arc, 'LINE_STRIP', {"pos": world_coors})

    region = bpy.context.region
    viewport_size = (region.width, region.height)

    shader_arc.bind()
    shader_arc.uniform_float("color", color)
    shader_arc.uniform_float("lineWidth", thickness)
    shader_arc.uniform_float("viewportSize", viewport_size)
    batch_arc.draw(shader_arc)
    
    if world_coors:
        # POINTS
        point_coors = [world_coors[0], world_coors[-1]]
        points(point_coors, thickness*3, color)

        line_coors = [center, world_coors[0], center, world_coors[-1]]
        lines_p2p(line_coors, thickness/2, color)
