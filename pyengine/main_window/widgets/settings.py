from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QSpinBox, QFileDialog, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class Settings(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.project = None
        self.setWindowTitle("PyEngine4 - Project Settings")
        self.resize(400, 400)
        title = QLabel("Project Settings", self)
        width = QLabel("Window Width", self)
        self.width_spin = QSpinBox(self)
        height = QLabel("Window Height", self)
        self.height_spin = QSpinBox(self)
        main_scene = QLabel("Main Scene", self)
        self.main_scene_edit = QLineEdit("", self)
        self.valid = QPushButton("Validate", self)

        title.setFont(QFont("arial", 20, 1))
        title.setAlignment(Qt.AlignHCenter)
        width.setAlignment(Qt.AlignHCenter)
        height.setAlignment(Qt.AlignHCenter)
        main_scene.setAlignment(Qt.AlignHCenter)
        self.width_spin.setMinimum(1)
        self.width_spin.setMaximum(2147483647)
        self.height_spin.setMinimum(1)
        self.height_spin.setMaximum(2147483647)
        self.valid.clicked.connect(self.validate)

        self.layout = QVBoxLayout()
        self.layout.addWidget(title)
        self.layout.addSpacing(40)
        self.layout.addWidget(width)
        self.layout.addWidget(self.width_spin)
        self.layout.addSpacing(20)
        self.layout.addWidget(height)
        self.layout.addWidget(self.height_spin)
        self.layout.addSpacing(20)
        self.layout.addWidget(main_scene)
        self.layout.addWidget(self.main_scene_edit)
        self.layout.addSpacing(40)
        self.layout.addWidget(self.valid)
        self.layout.setContentsMargins(50, 10, 50, 10)
        self.setLayout(self.layout)
    
    def validate(self):
        self.project.settings["width"] = self.width_spin.value()
        self.project.settings["height"] = self.height_spin.value()
        if len(self.main_scene_edit.text()) > 1:
            self.project.settings["mainScene"] = self.main_scene_edit.text()
        else:
            self.project.settings["mainScene"] = None
        self.project.save()
        self.parent.assets_explorer.update_project()
        self.parent.viewport.update_screen()
        main_scene = self.project.settings.get("mainScene", None)
        if main_scene is not None and self.project.get_scene(main_scene) is not None:
            self.parent.scene_tree.update_scene(self.project.get_scene(main_scene))
        self.close()
    
    def set_project(self, project):
        self.project = project
        self.width_spin.setValue(self.project.settings.get("width", 1080))
        self.height_spin.setValue(self.project.settings.get("height", 720))
        self.main_scene_edit.setText(self.project.settings.get("mainScene", ""))
