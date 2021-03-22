from PyQt5.QtWidgets import QWidget, QLabel, QSpinBox, QGridLayout
from PyQt5.QtCore import Qt


class BasicPhysicComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component

        self.name = QLabel("Basic Physics", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.gravity = QLabel("Gravity", self)
        self.gravity_spin = QSpinBox(self)

        self.gravity_spin.setValue(self.component.gravity)
        self.gravity_spin.valueChanged.connect(self.change_value)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0, 1, 5)
        self.layout.addWidget(self.gravity, 1, 0)
        self.layout.addWidget(self.gravity_spin, 1, 1, 1, 4)

        self.setLayout(self.layout)

    def change_value(self):
        self.component.gravity = self.gravity_spin.value()
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
