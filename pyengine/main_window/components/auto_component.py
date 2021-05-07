from PyQt5.QtWidgets import QWidget, QLabel, QSpinBox, QGridLayout, QCheckBox, QPushButton
from PyQt5.QtCore import Qt

from pyengine.common.utils import Vec2


class AutoComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component

        self.name = QLabel("Auto", self)
        self.delete_btn = QPushButton("Delete", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.move_name = QLabel("Movement", self)
        self.move_spins = [QSpinBox(self), QSpinBox(self)]
        self.rot_name = QLabel("Rotation", self)
        self.rot_spin = QSpinBox(self)
        self.active = QLabel("Active", self)
        self.active_check = QCheckBox(self)

        for i in self.move_spins:
            i.setRange(-2147483648, 2147483647)
        self.move_spins[0].setValue(self.component.move.x)
        self.move_spins[1].setValue(self.component.move.y)
        self.rot_spin.setRange(-2147483648, 2147483647)
        self.rot_spin.setValue(self.component.rotation)
        self.active_check.setChecked(component.active)
        self.active_check.clicked.connect(self.change_value)
        self.delete_btn.clicked.connect(self.delete)

        spins = self.move_spins + [self.rot_spin]
        for spin in spins:
            spin.valueChanged.connect(self.change_value)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 1, 1, 3)
        self.layout.addWidget(self.delete_btn, 0, 4)
        self.layout.addWidget(self.move_name, 1, 0)
        self.layout.addWidget(self.move_spins[0], 1, 1, 1, 2)
        self.layout.addWidget(self.move_spins[1], 1, 3, 1, 2)
        self.layout.addWidget(self.rot_name, 2, 0)
        self.layout.addWidget(self.rot_spin, 2, 1, 1, 4)
        self.layout.addWidget(self.active, 3, 0)
        self.layout.addWidget(self.active_check, 3, 1, 1, 4)

        self.setLayout(self.layout)

    def delete(self):
        self.parent.remove_component(comp=self.component.name)

    def change_value(self):
        self.component.move = Vec2(self.move_spins[0].value(), self.move_spins[1].value())
        self.component.rotation = self.rot_spin.value()
        self.component.active = self.active_check.isChecked()
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
