from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QSpinBox, QPushButton, QCheckBox
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
        number_mixer_channel = QLabel("Number Mixer Channel", self)
        self.number_mixer_channel_spin = QSpinBox(self)
        default_lang = QLabel("Current Language Name")
        self.default_lang_edit = QLineEdit("", self)
        self.debug_check = QCheckBox("Debug Mode", self)
        self.valid = QPushButton("Validate", self)

        title.setFont(QFont("arial", 20, 1))
        title.setAlignment(Qt.AlignHCenter)
        width.setAlignment(Qt.AlignHCenter)
        height.setAlignment(Qt.AlignHCenter)
        main_scene.setAlignment(Qt.AlignHCenter)
        number_mixer_channel.setAlignment(Qt.AlignHCenter)
        default_lang.setAlignment(Qt.AlignHCenter)
        self.width_spin.setRange(1, 2147483647)
        self.height_spin.setRange(1, 2147483647)
        self.number_mixer_channel_spin.setRange(1, 100)
        self.valid.clicked.connect(self.validate)

        self.layout = QVBoxLayout()
        self.layout.addWidget(title)
        self.layout.addSpacing(20)
        self.layout.addWidget(width)
        self.layout.addWidget(self.width_spin)
        self.layout.addSpacing(10)
        self.layout.addWidget(height)
        self.layout.addWidget(self.height_spin)
        self.layout.addSpacing(10)
        self.layout.addWidget(main_scene)
        self.layout.addWidget(self.main_scene_edit)
        self.layout.addSpacing(10)
        self.layout.addWidget(number_mixer_channel)
        self.layout.addWidget(self.number_mixer_channel_spin)
        self.layout.addSpacing(10)
        self.layout.addWidget(default_lang)
        self.layout.addWidget(self.default_lang_edit)
        self.layout.addSpacing(10)
        self.layout.addWidget(self.debug_check)
        self.layout.addSpacing(20)
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
        self.project.settings["numberMixerChannels"] = self.number_mixer_channel_spin.value()
        if len(self.default_lang_edit.text()) > 1:
            self.project.settings["defaultLang"] = self.default_lang_edit.text()
        else:
            self.project.settings["defaultLang"] = None
        self.project.settings["debug"] = self.debug_check.isChecked()
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
        self.number_mixer_channel_spin.setValue(self.project.settings.get("numberMixerChannels", 8))
        self.default_lang_edit.setText(self.project.settings.get("defaultLang", ""))
        self.debug_check.setChecked(self.project.settings.get("debug", False))
