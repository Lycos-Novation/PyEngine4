from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QFileDialog, QSpinBox
from PyQt5.QtCore import Qt

import os


class SpriteSheetComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component
        self.setAcceptDrops(True)

        self.name = QLabel("SpriteSheet", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.delete_btn = QPushButton("Delete", self)
        self.sprite = QLabel("Sprite", self)
        self.sprite_edit = QPushButton("Change Sprite", self)
        self.sprite_number = QLabel("Sprite Number")
        self.sprite_number_spins = [QSpinBox(self), QSpinBox(self)]
        self.current_sprite = QLabel("Current Sprite Index")
        self.current_sprite_spin = QSpinBox(self)

        for k, v in enumerate(self.sprite_number_spins):
            v.setMinimum(1)
            v.setValue(self.component.sprite_number[k])
            v.valueChanged.connect(self.change_value)
        self.current_sprite_spin.setMaximum(self.component.sprite_number[0] * self.component.sprite_number[1] - 1)
        self.current_sprite_spin.setValue(self.component.current_sprite)
        self.current_sprite_spin.valueChanged.connect(self.change_value)
        self.sprite_edit.clicked.connect(self.change_sprite)
        self.delete_btn.clicked.connect(self.delete)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 1, 1, 3)
        self.layout.addWidget(self.delete_btn, 0, 4)
        self.layout.addWidget(self.sprite, 1, 0)
        self.layout.addWidget(self.sprite_edit, 1, 1, 1, 4)
        self.layout.addWidget(self.sprite_number, 2, 0)
        for k, v in enumerate(self.sprite_number_spins):
            self.layout.addWidget(v, 2, 1+2*k, 1, 2)
        self.layout.addWidget(self.current_sprite, 3, 0)
        self.layout.addWidget(self.current_sprite_spin, 3, 1, 1, 4)
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
            self.change_spritesheet(data)
            e.accept()
            return
        super().dropEvent(e)

    def change_sprite(self):
        file_name = QFileDialog.getOpenFileName(
            self,
            "Open Texture",
            self.parent.parent.project.folders["textures"],
            "Texture (*.json)"
        )
        if len(file_name[0]) > 0:
            self.change_spritesheet(file_name[0])

    def change_spritesheet(self, file):
        self.component.sprite = os.path.basename(file.replace(".json", ""))
        self.change_value()

    def change_value(self):
        self.component.sprite_number = [i.value() for i in self.sprite_number_spins]
        self.component.current_sprite = self.current_sprite_spin.value()
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
