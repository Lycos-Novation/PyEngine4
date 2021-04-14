from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt


class TagComponent(QWidget):
    def __init__(self, parent, gameobject):
        super().__init__(parent)
        self.parent = parent
        self.gameobject = gameobject

        self.tag = QLabel("Tag", self)
        self.tag.setAlignment(Qt.AlignHCenter)
        self.tag_edit = QLineEdit(self)
        self.tag_edit.setText(gameobject.tag)

        self.tag_edit.textChanged.connect(self.change_value)

        self.layout = QGridLayout()
        self.layout.addWidget(self.tag, 0, 0)
        self.layout.addWidget(self.tag_edit, 1, 0)
        self.setLayout(self.layout)

    def change_value(self):
        self.component.tag = self.tag_edit.text()
        self.parent.parent.project.save()
        self.parent.parent.assets_explorer.open_folder(self.parent.parent.assets_explorer.current_folder)
        self.parent.parent.viewport.update_screen()
