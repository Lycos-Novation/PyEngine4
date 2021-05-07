from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout, QCheckBox, QSpinBox, QPushButton
from PyQt5.QtCore import Qt

from pyengine.common.utils import Vec2


class CollisionComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component

        names = self.component.callback.split(" - ") if self.component.callback is not None else ["", ""]

        self.name = QLabel("Collision", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.delete_btn = QPushButton("Delete", self)
        self.solid = QLabel("Is Solid", self)
        self.solid_check = QCheckBox(self)
        self.callback = QLabel("Callback", self)
        self.callback_script_edit = QLineEdit(names[0], self)
        self.callback_func_edit = QLineEdit(names[1], self)
        self.size = QLabel("Size", self)
        self.size_spins = [QSpinBox(self), QSpinBox(self)]

        self.solid_check.setChecked(self.component.solid)
        self.solid_check.clicked.connect(self.change_value)
        self.callback_script_edit.textChanged.connect(self.change_value)
        self.callback_func_edit.textChanged.connect(self.change_value)
        for k, i in enumerate(self.component.size):
            self.size_spins[k].setRange(0, 2147483647)
            self.size_spins[k].setValue(i)
            self.size_spins[k].valueChanged.connect(self.change_value)
        self.delete_btn.clicked.connect(self.delete)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 1, 1, 3)
        self.layout.addWidget(self.delete_btn, 0, 4)
        self.layout.addWidget(self.solid, 1, 0)
        self.layout.addWidget(self.solid_check, 1, 1, 1, 4)
        self.layout.addWidget(self.callback, 2, 0)
        self.layout.addWidget(self.callback_script_edit, 2, 1, 1, 2)
        self.layout.addWidget(self.callback_func_edit, 2, 3, 1, 2)
        self.layout.addWidget(self.size, 3, 0)
        self.layout.addWidget(self.size_spins[0], 3, 1, 1, 2)
        self.layout.addWidget(self.size_spins[1], 3, 3, 1, 2)

        self.setLayout(self.layout)

    def delete(self):
        self.parent.remove_component(comp=self.component.name)

    def change_value(self):
        self.component.solid = self.solid_check.isChecked()
        if len(self.callback_script_edit.text()) > 0 and len(self.callback_func_edit.text()) > 0:
            self.component.callback = self.callback_script_edit.text() + " - " + self.callback_func_edit.text()
        else:
            self.component.callback = None
        self.component.size = Vec2(*[i.value() for i in self.size_spins])
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
