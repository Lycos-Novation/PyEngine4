from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QFileDialog, QSpinBox, QCheckBox
from PyQt5.QtCore import Qt

import os


class MusicComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component
        self.setAcceptDrops(True)

        self.name = QLabel("Music", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.music_edit = QPushButton("Change Music", self)
        self.volume = QLabel("Volume", self)
        self.volume_spin = QSpinBox(self)
        self.play = QLabel("Play", self)
        self.play_check = QCheckBox(self)

        self.play_check.setChecked(component.play)
        self.play_check.clicked.connect(self.change_value)
        self.volume_spin.setRange(0, 100)
        self.volume_spin.setValue(component.volume)
        self.volume_spin.valueChanged.connect(self.change_value)
        self.music_edit.clicked.connect(self.change_music)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0, 1, 5)
        self.layout.addWidget(self.music_edit, 1, 0, 1, 5)
        self.layout.addWidget(self.volume, 2, 0)
        self.layout.addWidget(self.volume_spin, 2, 1, 1, 4)
        self.layout.addWidget(self.play, 3, 0)
        self.layout.addWidget(self.play_check, 3, 1, 1, 4)
        self.setLayout(self.layout)

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
        if file is not None:
            self.component.music = os.path.basename(file.replace(".json", ""))
        self.component.volume = self.volume_spin.value()
        self.component.play = self.play_check.isChecked()
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
