from PyQt5.QtWidgets import QWidget, QLabel, QDoubleSpinBox, QGridLayout
from PyQt5.QtCore import Qt


class TimeScaleComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component

        self.name = QLabel("TimeScale", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.spin = QDoubleSpinBox(self)

        self.spin.setValue(component.timescale)
        self.spin.valueChanged.connect(self.change_value)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0, 1, 4)
        self.layout.addWidget(self.spin, 1, 0, 1, 4)
        self.setLayout(self.layout)

    def change_value(self):
        self.component.timescale = self.spin.value()
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
