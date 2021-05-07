from PyQt5.QtWidgets import QWidget, QLabel, QSpinBox, QGridLayout, QPushButton
from PyQt5.QtCore import Qt


class BasicPhysicComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component

        self.name = QLabel("Basic Physics", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.delete_btn = QPushButton("Delete", self)
        self.gravity = QLabel("Gravity", self)
        self.gravity_spin = QSpinBox(self)

        self.gravity_spin.setRange(0, 2147483647)
        self.gravity_spin.setValue(self.component.gravity)
        self.gravity_spin.valueChanged.connect(self.change_value)
        self.delete_btn.clicked.connect(self.delete)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 1, 1, 3)
        self.layout.addWidget(self.delete_btn, 0, 4)
        self.layout.addWidget(self.gravity, 1, 0)
        self.layout.addWidget(self.gravity_spin, 1, 1, 1, 4)

        self.setLayout(self.layout)

    def delete(self):
        self.parent.remove_component(comp=self.component.name)

    def change_value(self):
        self.component.gravity = self.gravity_spin.value()
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
