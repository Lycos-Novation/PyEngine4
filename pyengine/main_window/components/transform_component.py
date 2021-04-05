from PyQt5.QtWidgets import QWidget, QLabel, QSpinBox, QGridLayout, QDoubleSpinBox
from PyQt5.QtCore import Qt

from pyengine.common.utils import Vec2


class TransformComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component
        
        self.name = QLabel("Transform", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.pos_name = QLabel("Position", self)
        self.pos_spins = [QSpinBox(self), QSpinBox(self)]
        self.rot_name = QLabel("Rotation", self)
        self.rot_spin = QSpinBox(self)
        self.scale_name = QLabel("Scale", self)
        self.scale_spins = [QDoubleSpinBox(self), QDoubleSpinBox(self)]

        for k, v in enumerate(self.component.position.coords()):
            self.pos_spins[k].setRange(-2147483648, 2147483647)
            self.pos_spins[k].setValue(v)
        self.rot_spin.setRange(-2147483648, 2147483647)
        self.rot_spin.setValue(self.component.rotation)
        for k, v in enumerate(self.component.scale.coords()):
            self.scale_spins[k].setRange(-2147483648, 2147483647)
            self.scale_spins[k].setValue(v)
            self.scale_spins[k].setSingleStep(0.01)

        spins = self.pos_spins + self.scale_spins + [self.rot_spin]
        for spin in spins:
            spin.valueChanged.connect(self.change_value)
        
        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0, 1, 5)
        self.layout.addWidget(self.pos_name, 1, 0)
        self.layout.addWidget(self.pos_spins[0], 1, 1, 1, 2)
        self.layout.addWidget(self.pos_spins[1], 1, 3, 1, 2)
        self.layout.addWidget(self.rot_name, 2, 0)
        self.layout.addWidget(self.rot_spin, 2, 1, 1, 4)
        self.layout.addWidget(self.scale_name, 3, 0)
        self.layout.addWidget(self.scale_spins[0], 3, 1, 1, 2)
        self.layout.addWidget(self.scale_spins[1], 3, 3, 1, 2)

        self.setLayout(self.layout)
    
    def change_value(self):
        self.component.position = Vec2(*(i.value() for i in self.pos_spins))
        self.component.rotation = self.rot_spin.value()
        self.component.scale = Vec2(*(i.value() for i in self.scale_spins))
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
