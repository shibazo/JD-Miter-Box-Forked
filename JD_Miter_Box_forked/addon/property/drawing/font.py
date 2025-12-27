import bpy

from bpy.props import IntProperty

from mathutils import Vector


class BM_Font(bpy.types.PropertyGroup):
    # 
    main_text_size: bpy.props.IntProperty(
        name = "Main Text Size",
        description = "Size of Main Panel Text",
        default = 18,
        min = 10
    )
    # 
    main_text_color: bpy.props.FloatVectorProperty(
        name = "Main Text Color",
        description = "Color of Main Panel text",
        subtype='COLOR',
        size = 3,
        default = (1.0, 1.0, 1.0),
        min = 0.0,
        max = 1.0
    )
    # 
    sub_text_size: bpy.props.IntProperty(
        name = "Sub Text Size",
        description = "Size of Sub Panel Text",
        default = 15,
        min = 10
    )
    # 
    sub_text_color: bpy.props.FloatVectorProperty(
        name = "Sub Text Color",
        description = "Color of Sub Panel text",
        subtype='COLOR',
        size = 3,
        default = (1.0, 1.0, 1.0),
        min = 0.0,
        max = 1.0
    )

font_prefs = [{'main_text_size': "Size of Main Panel Text"},
              {'main_text_color': "Color of Main Panel Text"},
              {'sub_text_size': "Size of Sub Panel Text"},
              {'sub_text_color': "Color of Sub Panel Text"},
]

def draw_font(prefs, layout):

    column = layout.column()
    column.label(text="Font Sizes And Colors", icon='FILE_FONT')

    # size
    box = column.box()

    for item in font_prefs:

        if item == 0:
            row = box.row()
            row.separator()
            continue            

        for prop, text in item.items():
            row = box.row()
            # row.prop(prefs.font, prop, text=text)
            col = row.column().split()
            col.label(text=text)
            col.prop(prefs.font, prop, text='')
