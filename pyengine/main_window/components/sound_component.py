from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QFileDialog, QSpinBox, QCheckBox
from PyQt5.QtCore import Qt

import os


class SoundComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component
        self.setAcceptDrops(True)

        self.name = QLabel("Sound", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.delete_btn = QPushButton("Delete", self)
        self.music_edit = QPushButton("Change Sound", self)
        self.volume = QLabel("Volume", self)
        self.volume_spin = QSpinBox(self)

        self.volume_spin.setRange(0, 100)
        self.volume_spin.setValue(component.volume)
        self.volume_spin.valueChanged.connect(self.change_value)
        self.music_edit.clicked.connect(self.change_music)
        self.delete_btn.clicked.connect(self.delete)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 1, 1, 3)
        self.layout.addWidget(self.delete_btn, 0, 4)
        self.layout.addWidget(self.music_edit, 1, 0, 1, 5)
        self.layout.addWidget(self.volume, 2, 0)
        self.layout.addWidget(self.volume_spin, 2, 1, 1, 4)
        self.setLayout(self.layout)

    def delete(self):
        self.parent.remove_component(self.component.name)

    def dragEnterEvent(self, e) -> None:
        if e.mimeData().hasFormat("assets/sound"):
            e.accept()
        else:
            super().dragEnterEvent(e)

    def dragMoveEvent(self, e) -> None:
        if e.mimeData().hasFormat("assets/sound"):
            e.setDropAction(Qt.CopyAction)
            e.accept()
        else:
            super().dragMoveEvent(e)

    def dropEvent(self, e) -> None:
        if e.mimeData().hasFormat("assets/sound"):
            data = str(e.mimeData().data("assets/sound"), "utf-8")
            self.change_value(data)
            e.accept()
            return
        super().dropEvent(e)

    def change_music(self):
        file_name = QFileDialog.getOpenFileName(
            self,
            "Open Sound",
            self.parent.parent.project.folders["sounds"],
            "Sound (*.json)"
        )
        if len(file_name[0]) > 0:
            self.change_value(file_name[0])

    def change_value(self, file=None):
        if file is not None and isinstance(file, str):
            self.component.sound = os.path.basename(file.replace(".json", ""))
        self.component.volume = self.volume_spin.value()
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
