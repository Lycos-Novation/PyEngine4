from PyQt5.QtWidgets import QWidget, QLabel, QSpinBox, QGridLayout, QCheckBox
from PyQt5.QtCore import Qt


class AutoComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component

        self.name = QLabel("Auto", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.move_name = QLabel("Movement", self)
        self.move_spins = [QSpinBox(self), QSpinBox(self)]
        self.rot_name = QLabel("Rotation", self)
        self.rot_spin = QSpinBox(self)
        self.active = QLabel("Active", self)
        self.active_check = QCheckBox(self)

        for k, v in enumerate(self.component.move):
            self.move_spins[k].setRange(-2147483648, 2147483647)
            self.move_spins[k].setValue(v)
        self.rot_spin.setRange(-2147483648, 2147483647)
        self.rot_spin.setValue(self.component.rotation)
        self.active_check.setChecked(component.active)
        self.active_check.clicked.connect(self.change_value)

        spins = self.move_spins + [self.rot_spin]
        for spin in spins:
            spin.valueChanged.connect(self.change_value)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0, 1, 5)
        self.layout.addWidget(self.move_name, 1, 0)
        self.layout.addWidget(self.move_spins[0], 1, 1, 1, 2)
        self.layout.addWidget(self.move_spins[1], 1, 3, 1, 2)
        self.layout.addWidget(self.rot_name, 2, 0)
        self.layout.addWidget(self.rot_spin, 2, 1, 1, 4)
        self.layout.addWidget(self.active, 3, 0)
        self.layout.addWidget(self.active_check, 3, 1, 1, 4)

        self.setLayout(self.layout)

    def change_value(self):
        self.component.move = [i.value() for i in self.move_spins]
        self.component.rotation = self.rot_spin.value()
        self.component.active = self.active_check.isChecked()
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
