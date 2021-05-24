from PyQt5.QtWidgets import QWidget, QLabel, QSpinBox, QGridLayout, QColorDialog, QPushButton, QCheckBox, QDoubleSpinBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

from pyengine.common.utils import Color, Vec2


class ParticleComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component

        self.name = QLabel("Particle", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.delete_btn = QPushButton("Delete", self)
        self.color = QLabel("Color", self)
        self.color_spins = [QSpinBox(self), QSpinBox(self), QSpinBox(self), QSpinBox(self)]
        self.color_picker = QPushButton("Color Picker")
        self.final_color = QLabel("Final Color")
        self.final_color_spins = [QSpinBox(self), QSpinBox(self), QSpinBox(self), QSpinBox(self)]
        self.final_color_picker = QPushButton("Color Picker")
        self.size_name = QLabel("Size", self)
        self.size_spins = [QSpinBox(self), QSpinBox(self)]
        self.final_size_name = QLabel("Final Size", self)
        self.final_size_spins = [QSpinBox(self), QSpinBox(self)]
        self.angle_range_name = QLabel("Angle", self)
        self.angle_range_spins = [QSpinBox(self), QSpinBox(self)]
        self.force_range_name = QLabel("Force", self)
        self.force_range_spins = [QSpinBox(self), QSpinBox(self)]
        self.lifetime = QLabel("Life Time")
        self.lifetime_spin = QSpinBox(self)
        self.spawn_time = QLabel("Spawn Time")
        self.spawn_time_spin = QDoubleSpinBox(self)

        self.color_picker.clicked.connect(self.select_color)
        self.lifetime_spin.setRange(-2147483648, 2147483647)
        self.lifetime_spin.setValue(self.component.lifetime)
        self.lifetime_spin.valueChanged.connect(self.change_value)
        self.spawn_time_spin.setRange(-2147483648, 2147483647)
        self.spawn_time_spin.setValue(self.component.spawn_time)
        self.spawn_time_spin.setSingleStep(0.01)
        self.spawn_time_spin.valueChanged.connect(self.change_value)
        for k, v in enumerate(component.color.rgba()):
            self.color_spins[k].setRange(0, 255)
            self.color_spins[k].setValue(v)
            self.color_spins[k].valueChanged.connect(self.change_value)

        self.final_color_picker.clicked.connect(self.select_final_color)
        for k, v in enumerate(component.final_color.rgba()):
            self.final_color_spins[k].setRange(0, 255)
            self.final_color_spins[k].setValue(v)
            self.final_color_spins[k].valueChanged.connect(self.change_value)

        for k, v in enumerate(self.component.size.coords()):
            self.size_spins[k].setRange(-2147483648, 2147483647)
            self.size_spins[k].setValue(v)

        for k, v in enumerate(self.component.final_size.coords()):
            self.final_size_spins[k].setRange(-2147483648, 2147483647)
            self.final_size_spins[k].setValue(v)

        for k, v in enumerate(self.component.angle_range.coords()):
            self.angle_range_spins[k].setRange(0, 359)
            self.angle_range_spins[k].setValue(v)

        for k, v in enumerate(self.component.force_range.coords()):
            self.force_range_spins[k].setRange(-2147483648, 2147483647)
            self.force_range_spins[k].setValue(v)

        spins = self.size_spins + self.final_size_spins + self.angle_range_spins + self.force_range_spins
        for spin in spins:
            spin.valueChanged.connect(self.change_value)

        self.delete_btn.clicked.connect(self.delete)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 1, 1, 3)
        self.layout.addWidget(self.delete_btn, 0, 4)
        self.layout.addWidget(self.color, 1, 0)
        for i in range(len(self.color_spins)):
            self.layout.addWidget(self.color_spins[i], 1, 1+i)
        self.layout.addWidget(self.color_picker, 2, 0, 1, 5)
        self.layout.addWidget(self.final_color, 3, 0)
        for i in range(len(self.final_color_spins)):
            self.layout.addWidget(self.final_color_spins[i], 3, 1+i)
        self.layout.addWidget(self.final_color_picker, 4, 0, 1, 5)
        self.layout.addWidget(self.size_name, 5, 0)
        self.layout.addWidget(self.size_spins[0], 5, 1, 1, 2)
        self.layout.addWidget(self.size_spins[1], 5, 3, 1, 2)
        self.layout.addWidget(self.final_size_name, 6, 0)
        self.layout.addWidget(self.final_size_spins[0], 6, 1, 1, 2)
        self.layout.addWidget(self.final_size_spins[1], 6, 3, 1, 2)
        self.layout.addWidget(self.angle_range_name, 7, 0)
        self.layout.addWidget(self.angle_range_spins[0], 7, 1, 1, 2)
        self.layout.addWidget(self.angle_range_spins[1], 7, 3, 1, 2)
        self.layout.addWidget(self.force_range_name, 8, 0)
        self.layout.addWidget(self.force_range_spins[0], 8, 1, 1, 2)
        self.layout.addWidget(self.force_range_spins[1], 8, 3, 1, 2)
        self.layout.addWidget(self.lifetime, 9, 0)
        self.layout.addWidget(self.lifetime_spin, 9, 1, 1, 4)
        self.layout.addWidget(self.spawn_time, 10, 0)
        self.layout.addWidget(self.spawn_time_spin, 10, 1, 1, 4)
        self.setLayout(self.layout)

    def delete(self):
        self.parent.remove_component(comp=self.component.name)

    def select_color(self):
        color = QColorDialog.getColor(QColor(*self.component.color.rgba()), parent=self)
        if color.isValid():
            self.color_spins[0].setValue(color.red())
            self.color_spins[1].setValue(color.green())
            self.color_spins[2].setValue(color.blue())
            self.color_spins[3].setValue(color.alpha())
            self.change_value(color=[color.red(), color.green(), color.blue(), color.alpha()])

    def select_final_color(self):
        color = QColorDialog.getColor(QColor(*self.component.final_color.rgba()), parent=self)
        if color.isValid():
            self.final_color_spins[0].setValue(color.red())
            self.final_color_spins[1].setValue(color.green())
            self.final_color_spins[2].setValue(color.blue())
            self.final_color_spins[3].setValue(color.alpha())
            self.change_value(final_color=[color.red(), color.green(), color.blue(), color.alpha()])

    def change_value(self, _=None, color=None, final_color=None):
        if color is None:
            self.component.color = Color.from_rgba(*(i.value() for i in self.color_spins))
        else:
            self.component.color = Color.from_rgba(*color)

        if final_color is None:
            self.component.final_color = Color.from_rgba(*(i.value() for i in self.final_color_spins))
        else:
            self.component.final_color = Color.from_rgba(*final_color)

        self.component.size = Vec2(*(i.value() for i in self.size_spins))
        self.component.final_size = Vec2(*(i.value() for i in self.final_size_spins))
        self.component.angle_range = Vec2(*(i.value() for i in self.angle_range_spins))
        self.component.forge_range = Vec2(*(i.value() for i in self.force_range_spins))
        self.component.lifetime = self.lifetime_spin.value()
        self.component.spawn_time = self.spawn_time_spin.value()

        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
