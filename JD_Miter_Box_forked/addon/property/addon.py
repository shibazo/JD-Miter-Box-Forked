import bpy

from bpy.props import PointerProperty

from ..utility.addon import addon_name, get_prefs

from .drawing.color import BM_Color, draw_color
from .drawing.size import BM_Size, draw_size
from .drawing.font import BM_Font, draw_font
from .drawing.options import BM_Options, draw_options


class BM_Props(bpy.types.AddonPreferences):
    bl_idname = addon_name

    color : PointerProperty(type=BM_Color)
    size : PointerProperty(type=BM_Size)
    font : PointerProperty(type=BM_Font)
    options : PointerProperty(type=BM_Options)

    def draw(self, context):

        prefs = get_prefs()

        layout = self.layout

        # General settings
        box = layout.box()

        # Drawing settings
        box = layout.box()

        row = box.row()

        draw_color(prefs, row)
        # box.separator()
        draw_size(prefs, row)

        row = box.row()

        draw_font(prefs, row)

        row = box.row()

        draw_options(prefs, row)
