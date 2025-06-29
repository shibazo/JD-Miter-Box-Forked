import bpy

from .drawing.color import BM_Color
from .drawing.size import BM_Size
from .drawing.font import BM_Font
from .addon import BM_Props

# register BM_Props last!
classes = (
    BM_Color,
    BM_Size,
    BM_Font,
    BM_Props,
)


def register_properties():
    from bpy.utils import register_class
    for cls in classes:
        register_class(cls)


def unregister_properties():
    from bpy.utils import unregister_class
    for cls in reversed(classes):
        unregister_class(cls)