from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QSpinBox
from PyQt5.QtCore import Qt

from pyengine.common.utils import Vec2


class CameraComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component

        self.name = QLabel("Camera", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.pos_name = QLabel("Position", self)
        self.pos_spins = [QSpinBox(self), QSpinBox(self)]

        for k, v in enumerate(self.component.position.coords()):
            self.pos_spins[k].setRange(-2147483648, 2147483647)
            self.pos_spins[k].setValue(v)
            self.pos_spins[k].valueChanged.connect(self.change_value)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0, 1, 4)
        self.layout.addWidget(self.pos_name, 1, 0)
        self.layout.addWidget(self.pos_spins[0], 1, 1, 1, 2)
        self.layout.addWidget(self.pos_spins[1], 1, 3, 1, 2)
        self.setLayout(self.layout)

    def change_value(self):
        self.component.position = Vec2(*(i.value() for i in self.pos_spins))
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
