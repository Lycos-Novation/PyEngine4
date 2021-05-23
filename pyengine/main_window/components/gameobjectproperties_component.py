from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QLineEdit, QSpinBox
from PyQt5.QtCore import Qt


class GameObjectPropertiesComponent(QWidget):
    def __init__(self, parent, gameobject):
        super().__init__(parent)
        self.parent = parent
        self.gameobject = gameobject

        self.tag = QLabel("Tag", self)
        self.tag.setAlignment(Qt.AlignHCenter)
        self.tag_edit = QLineEdit(self)
        self.tag_edit.setText(gameobject.tag)
        self.zindex = QLabel("Z-Index", self)
        self.zindex.setAlignment(Qt.AlignHCenter)
        self.zindex_edit = QSpinBox(self)
        self.zindex_edit.setRange(-2147483648, 2147483647)
        self.zindex_edit.setValue(gameobject.zindex)

        self.tag_edit.textChanged.connect(self.change_value)
        self.zindex_edit.textChanged.connect(self.change_value)

        self.layout = QGridLayout()
        self.layout.addWidget(self.tag, 0, 0)
        self.layout.addWidget(self.tag_edit, 1, 0)
        self.layout.addWidget(self.zindex, 2, 0)
        self.layout.addWidget(self.zindex_edit, 3, 0)
        self.setLayout(self.layout)

    def change_value(self):
        self.gameobject.tag = self.tag_edit.text()
        self.gameobject.zindex = self.zindex_edit.value()
        self.parent.parent.project.save()
        self.parent.parent.assets_explorer.open_folder(self.parent.parent.assets_explorer.current_folder)
        self.parent.parent.viewport.update_screen()
