from PyQt5.QtWidgets import QWidget, QLabel, QSpinBox, QGridLayout, QColorDialog, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

from pyengine.common.utils import Color


class ColorComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component
        
        self.name = QLabel("Color", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.color_spins = [QSpinBox(self), QSpinBox(self), QSpinBox(self), QSpinBox(self)]
        self.color_picker = QPushButton("Color Picker")

        self.color_picker.clicked.connect(self.select_color)
        for k, v in enumerate(component.color.rgba()):
            self.color_spins[k].setRange(0, 255)
            self.color_spins[k].setValue(v)
            self.color_spins[k].valueChanged.connect(self.change_value)
        
        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0, 1, 4)
        for i in range(len(self.color_spins)):
            self.layout.addWidget(self.color_spins[i], 1, i)
        self.layout.addWidget(self.color_picker, 2, 0, 1, 4)
        self.setLayout(self.layout)

    def select_color(self):
        color = QColorDialog.getColor(QColor(*self.component.color.rgba()), parent=self)
        if color.isValid():
            self.color_spins[0].setValue(color.red())
            self.color_spins[1].setValue(color.green())
            self.color_spins[2].setValue(color.blue())
            self.color_spins[3].setValue(color.alpha())
            self.change_value(color=[color.red(), color.green(), color.blue(), color.alpha()])
    
    def change_value(self, _=None, color=None):
        if color is None:
            self.component.color = Color.from_rgba(*(i.value() for i in self.color_spins))
        else:
            self.component.color = Color.from_rgba(*color)
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
