from PyQt5.QtWidgets import QWidget, QLabel, QSpinBox, QGridLayout
from PyQt5.QtCore import Qt

from pyengine.common.utils import Color


class ColorComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component
        
        self.name = QLabel("Color", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.color_spins = [QSpinBox(self), QSpinBox(self), QSpinBox(self), QSpinBox(self)]

        for k, v in enumerate(component.color.rgba()):
            self.color_spins[k].setRange(0, 255)
            self.color_spins[k].setValue(v)
            self.color_spins[k].valueChanged.connect(self.change_value)
        
        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0, 1, 4)
        for i in range(len(self.color_spins)):
            self.layout.addWidget(self.color_spins[i], 1, i)
        self.setLayout(self.layout)
    
    def change_value(self):
        self.component.color = Color.from_rgba(*(i.value() for i in self.color_spins))
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
