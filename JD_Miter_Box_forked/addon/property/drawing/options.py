import bpy

from bpy.props import IntProperty

from mathutils import Vector


class BM_Options(bpy.types.PropertyGroup):
    #
    normal_size: bpy.props.IntProperty(
        name = "Face Normal Size",
        description = "Face Normal Vector Size",
        default = 2,
        min = 2
    )
    # 
    normal_color: bpy.props.FloatVectorProperty(
        name = "Face Normal Color",
        description = "Face Normail Vector Color",
        subtype='COLOR',
        size = 3,
        default = (0.133, 0.867, 0.867),
        min = 0.0,
        max = 1.0
    )
    #
    show_circle: bpy.props.BoolProperty(
        name = "Show Circle",
        description = "Show a circle indicating the selection face when in Align to Face Mode.",
        default = False,
    )
    #
    circle_size: bpy.props.IntProperty(
        name = "Circle Size",
        description = "Circle Size",
        default = 1,
        min = 1,
        max = 5
    )
    # 
    circle_border_color: bpy.props.FloatVectorProperty(
        name = "Border Color",
        description = "Circle Border Color",
        subtype='COLOR',
        size = 4,
        default = (1.0, 1.0, 1.0, 1.0),
        min = 0.0,
        max = 1.0
    )
    # 
    circle_fill_color: bpy.props.FloatVectorProperty(
        name = "Fill Color",
        description = "Circle Fill Color",
        subtype='COLOR',
        size = 4,
        default = (1.0, 1.0, 1.0, 0.3),
        min = 0.0,
        max = 1.0
    )


options_prefs = [{'normal_size': "Size of Normal Select Face"},
                 {'normal_color': "Color of Normal Select Face"},
                 {'show_circle': "show Circle"},
                 {'circle_size': "Circle Size"},
                 {'circle_border_color': "Circle Border Color"},
                 {'circle_fill_color': "Circle Fill Color"},
]

def draw_options(prefs, layout):

    column = layout.column()
    column.label(text="Options", icon='OPTIONS')

    box = column.box()

    row = box.row()
    row.label(text='Align to Face Mode Options')

    row = box.row()

    row.label(text="Normal(of selection face)")
    row.prop(prefs.options, "normal_size" , text = "Size" )
    row.prop(prefs.options, "normal_color" , text = "" )

    row = box.row()
    row.prop(prefs.options, "show_circle")
    row = box.row()
    row.prop(prefs.options, "circle_size" , text = "Size" )
    row.prop(prefs.options, "circle_border_color" , text = "Border" )
    row.prop(prefs.options, "circle_fill_color" , text = "Fill" )
