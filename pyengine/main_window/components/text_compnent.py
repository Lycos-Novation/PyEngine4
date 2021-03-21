from PyQt5.QtWidgets import QWidget, QLabel, QSpinBox, QGridLayout, QLineEdit, QCheckBox
from PyQt5.QtCore import Qt


class TextComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component

        self.name = QLabel("Text", self)
        self.text = QLabel("Text", self)
        self.text_edit = QLineEdit(self.component.text, self)
        self.font_name = QLabel("Font Name", self)
        self.font_name_edit = QLineEdit(self.component.font_name, self)
        self.font_size = QLabel("Font Size", self)
        self.font_size_spin = QSpinBox(self)
        self.font_color_name = QLabel("Font Color", self)
        self.font_color_spins = [QSpinBox(self), QSpinBox(self), QSpinBox(self), QSpinBox(self)]
        self.font_bold = QLabel("Font Bold", self)
        self.font_bold_check = QCheckBox(self)
        self.font_italic = QLabel("Font Italic", self)
        self.font_italic_check = QCheckBox(self)
        self.font_underline = QLabel("Font Underline", self)
        self.font_underline_check = QCheckBox(self)
        self.font_antialias = QLabel("Font Antialias", self)
        self.font_antialias_check = QCheckBox(self)

        self.name.setAlignment(Qt.AlignHCenter)
        self.text_edit.textChanged.connect(self.change_value)
        self.font_name_edit.textChanged.connect(self.change_value)
        self.font_size_spin.setValue(self.component.font_size)
        self.font_size_spin.valueChanged.connect(self.change_value)
        self.font_bold_check.setChecked(self.component.font_bold)
        self.font_bold_check.clicked.connect(self.change_value)
        self.font_italic_check.setChecked(self.component.font_italic)
        self.font_italic_check.clicked.connect(self.change_value)
        self.font_underline_check.setChecked(self.component.font_underline)
        self.font_underline_check.clicked.connect(self.change_value)
        self.font_antialias_check.setChecked(self.component.font_antialias)
        self.font_antialias_check.clicked.connect(self.change_value)
        for k, v in enumerate(component.font_color):
            self.font_color_spins[k].setMinimum(0)
            self.font_color_spins[k].setMaximum(255)
            self.font_color_spins[k].setValue(v)
            self.font_color_spins[k].valueChanged.connect(self.change_value)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0, 1, 5)
        self.layout.addWidget(self.text, 1, 0)
        self.layout.addWidget(self.text_edit, 1, 1, 1, 4)
        self.layout.addWidget(self.font_name, 2, 0)
        self.layout.addWidget(self.font_name_edit, 2, 1, 1, 4)
        self.layout.addWidget(self.font_size, 3, 0)
        self.layout.addWidget(self.font_size_spin, 3, 1, 1, 4)
        self.layout.addWidget(self.font_color_name, 4, 0)
        for i in range(len(self.font_color_spins)):
            self.layout.addWidget(self.font_color_spins[i], 4, i+1)
        self.layout.addWidget(self.font_bold, 5, 0)
        self.layout.addWidget(self.font_bold_check, 5, 1, 1, 4)
        self.layout.addWidget(self.font_italic, 6, 0)
        self.layout.addWidget(self.font_italic_check, 6, 1, 1, 4)
        self.layout.addWidget(self.font_underline, 7, 0)
        self.layout.addWidget(self.font_underline_check, 7, 1, 1, 4)
        self.layout.addWidget(self.font_antialias, 8, 0)
        self.layout.addWidget(self.font_antialias_check, 8, 1, 1, 4)
        self.setLayout(self.layout)

    def change_value(self):
        self.component.text = self.text_edit.text()
        self.component.font_name = self.font_name_edit.text()
        self.component.font_size = self.font_size_spin.value()
        self.component.font_color = [i.value() for i in self.font_color_spins]
        self.component.font_bold = self.font_bold_check.isChecked()
        self.component.font_italic = self.font_italic_check.isChecked()
        self.component.font_underline = self.font_underline_check.isChecked()
        self.component.font_antialias = self.font_antialias_check.isChecked()
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
