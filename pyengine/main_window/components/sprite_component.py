from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QFileDialog
from PyQt5.QtCore import Qt

import os


class SpriteComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component
        self.setAcceptDrops(True)
        
        self.name = QLabel("Sprite", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.delete_btn = QPushButton("Delete", self)
        self.sprite_edit = QPushButton("Change Sprite", self)

        self.sprite_edit.clicked.connect(self.change_value)
        self.delete_btn.clicked.connect(self.delete)
        
        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 1, 1, 3)
        self.layout.addWidget(self.delete_btn, 0, 4)
        self.layout.addWidget(self.sprite_edit, 1, 0, 1, 5)
        self.setLayout(self.layout)

    def delete(self):
        self.parent.remove_component(comp=self.component.name)

    def dragEnterEvent(self, e) -> None:
        if e.mimeData().hasFormat("assets/texture"):
            e.accept()
        else:
            super().dragEnterEvent(e)

    def dragMoveEvent(self, e) -> None:
        if e.mimeData().hasFormat("assets/texture"):
            e.setDropAction(Qt.CopyAction)
            e.accept()
        else:
            super().dragMoveEvent(e)

    def dropEvent(self, e) -> None:
        if e.mimeData().hasFormat("assets/texture"):
            data = str(e.mimeData().data("assets/texture"), "utf-8")
            self.change_sprite(data)
            e.accept()
            return
        super().dropEvent(e)
    
    def change_value(self):
        file_name = QFileDialog.getOpenFileName(
            self,
            "Open Texture",
            self.parent.parent.project.folders["textures"],
            "Texture (*.json)"
        )
        if len(file_name[0]) > 0:
            self.change_sprite(file_name[0])

    def change_sprite(self, file):
        self.component.sprite = os.path.basename(file.replace(".json", ""))
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
