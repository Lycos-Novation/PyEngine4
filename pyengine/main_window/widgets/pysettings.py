from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QSpinBox, QFileDialog, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class PySettings(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.project = None
        self.setWindowTitle("PyEngine4 - Engine Settings")
        self.resize(200, 200)
        title = QLabel("Engine Settings", self)
        editor = QLabel("Script Editor", self)
        self.editor_select = QPushButton("Select Editor", self)
        self.current_editor = self.parent.engine_settings.values.get("editor", None)
        self.valid = QPushButton("Validate", self)

        title.setFont(QFont("arial", 20, 1))
        title.setAlignment(Qt.AlignHCenter)
        editor.setAlignment(Qt.AlignHCenter)
        self.editor_select.clicked.connect(self.select_editor)
        self.valid.clicked.connect(self.validate)

        self.layout = QVBoxLayout()
        self.layout.addWidget(title)
        self.layout.addSpacing(40)
        self.layout.addWidget(editor)
        self.layout.addWidget(self.editor_select)
        self.layout.addSpacing(40)
        self.layout.addWidget(self.valid)
        self.layout.setContentsMargins(50, 10, 50, 10)
        self.setLayout(self.layout)

    def select_editor(self):
        file_name = QFileDialog.getOpenFileName(self, "Open Editor", filter="Editor (*.exe)")
        if len(file_name[0]) > 0:
            self.current_editor = file_name[0]

    def validate(self):
        self.parent.engine_settings.values["editor"] = self.current_editor
        self.parent.engine_settings.save()
        self.close()
