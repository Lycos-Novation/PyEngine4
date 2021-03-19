from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QFileDialog
from PyQt5.QtCore import Qt

import os


class SpriteComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component
        
        self.name = QLabel("Sprite", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.sprite_edit = QPushButton("Change Sprite", self)

        self.sprite_edit.clicked.connect(self.change_value)
        
        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0)
        self.layout.addWidget(self.sprite_edit, 1, 0)
        self.setLayout(self.layout)
    
    def change_value(self):
        file_name = QFileDialog.getOpenFileName(
            self,
            "Open Texture",
            self.parent.parent.project.folders["textures"],
            "Texture (*.json)"
        )
        if len(file_name[0]) > 0:
            self.component.sprite = os.path.basename(file_name[0].replace(".json", ""))
            self.parent.parent.project.save()
            self.parent.parent.viewport.update_screen()
