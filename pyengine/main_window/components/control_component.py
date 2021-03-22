from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QComboBox, QGridLayout, QSpinBox
from PyQt5.QtCore import Qt


class ControlComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component
        self.types = ["FOURDIRECTION", "UPDOWN", "LEFTRIGHT", "CLASSICJUMP"]

        self.name = QLabel("Control", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.key_labels = [
            QLabel("Up/Jump Key", self),
            QLabel("Down Key", self),
            QLabel("Left Key", self),
            QLabel("Right Key", self)
        ]
        self.key_edits = [
            QLineEdit(self.component.keys["UPJUMP"], self),
            QLineEdit(self.component.keys["DOWN"], self),
            QLineEdit(self.component.keys["LEFT"], self),
            QLineEdit(self.component.keys["RIGHT"], self)
        ]
        self.control_type = QLabel("Control Type", self)
        self.control_type_combobox = QComboBox(self)
        self.speed = QLabel("Speed", self)
        self.speed_spin = QSpinBox(self)

        for i in self.key_edits:
            i.textChanged.connect(self.change_value)
        self.control_type_combobox.addItems(self.types)
        self.control_type_combobox.setCurrentIndex(self.types.index(self.component.control_type))
        self.control_type_combobox.currentIndexChanged.connect(self.change_value)
        self.speed_spin.setValue(self.component.speed)
        self.speed_spin.valueChanged.connect(self.change_value)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0, 1, 5)
        for i in range(len(self.key_labels)):
            self.layout.addWidget(self.key_labels[i], i+1, 0)
            self.layout.addWidget(self.key_edits[i], i+1, 1, 1, 4)
        self.layout.addWidget(self.control_type, len(self.key_labels)+1, 0)
        self.layout.addWidget(self.control_type_combobox, len(self.key_labels)+1, 1, 1, 4)
        self.layout.addWidget(self.speed, len(self.key_labels)+2, 0)
        self.layout.addWidget(self.speed_spin, len(self.key_labels)+2, 1, 1, 4)
        self.setLayout(self.layout)

    def change_value(self):
        self.component.control_type = self.types[self.control_type_combobox.currentIndex()]
        self.component.keys = {
            "UPJUMP": self.key_edits[0].text(),
            "DOWN": self.key_edits[1].text(),
            "LEFT": self.key_edits[2].text(),
            "RIGHT": self.key_edits[3].text()
        }
        self.component.speed = self.speed_spin.value()
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
