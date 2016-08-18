# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8-80 compliant>

bl_info = {
    "name": "Mesh Layers",
    "author": "Jiri Hnidek",
    "blender": (2, 74, 0),
    "location": "Properties > Mesh",
    "description": "Manipulation and visualization of mesh layers.",
    "warning": "",
    "category": "3D View"}

if "bpy" in locals():
    import importlib
    if "ui" in locals():
        importlib.reload(ui)
else:
    import bpy
    from . import ui


def register():
    """
    Function for registering this Add-on.
    :return: None
    """
    bpy.utils.register_module(__name__)


def unregister():
    """
    Function for unregistrating of this Add-on
    :return: None
    """
    bpy.utils.unregister_module(__name__)


if __name__ == '__main__':
    register()
