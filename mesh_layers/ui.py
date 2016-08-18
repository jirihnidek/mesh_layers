import bpy
from bpy.types import Panel


class DATA_PT_data_layer(MeshButtonsPanel, Panel):
    bl_label = "Data Layers"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "data"

    @classmethod
    def poll(cls, context):
        obj = context.object
        return obj and obj.type == 'MESH'

    def draw(self, context):
        layout = self.layout
        obj = context.object
