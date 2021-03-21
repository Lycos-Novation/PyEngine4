from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout, QCheckBox
from PyQt5.QtCore import Qt


class CollisionComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component

        names = self.component.callback.split(" - ") if self.component.callback is not None else ["", ""]

        self.name = QLabel("Collision", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.solid = QLabel("Is Solid", self)
        self.solid_check = QCheckBox(self)
        self.callback = QLabel("Callback", self)
        self.callback_script_edit = QLineEdit(names[0], self)
        self.callback_func_edit = QLineEdit(names[1], self)

        self.solid_check.setChecked(self.component.solid)
        self.solid_check.clicked.connect(self.change_value)
        self.callback_script_edit.textChanged.connect(self.change_value)
        self.callback_func_edit.textChanged.connect(self.change_value)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0, 1, 5)
        self.layout.addWidget(self.solid, 1, 0)
        self.layout.addWidget(self.solid_check, 1, 1, 1, 4)
        self.layout.addWidget(self.callback, 2, 0)
        self.layout.addWidget(self.callback_script_edit, 2, 1, 1, 2)
        self.layout.addWidget(self.callback_func_edit, 2, 3, 1, 2)

        self.setLayout(self.layout)

    def change_value(self):
        self.component.solid = self.solid_check.isChecked()
        if len(self.callback_script_edit.text()) > 0 and len(self.callback_func_edit.text()) > 0:
            self.component.callback = self.callback_script_edit.text() + " - " + self.callback_func_edit.text()
        else:
            self.component.callback = None
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
