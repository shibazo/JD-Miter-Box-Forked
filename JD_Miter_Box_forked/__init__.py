# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from .addon.utility import addon

bl_info = {
    "name" : "Miter Box (Forked)",
    "author" : "João Desager / (Shibazo)",
    "description" : "Collection of Mesh Editing tools",
    "blender" : (3, 3, 4),
    "version" : (0, 0, 6),
    "location" : "Edit Mode > Context Menu > MiterBox, N Panel > MB",
    "warning" : "",
    "category" : "Generic",
    "tagline" : "Forked and updated for Blender 4.x"
}

addon.addon_name = __name__

def register():
    from .addon.register import register_addon
    register_addon()

def unregister():
    from .addon.register import unregister_addon
    unregister_addon()
