from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QFileDialog
from PyQt5.QtCore import Qt


class PathComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component
        
        self.name = QLabel("Path", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.path_edit = QPushButton("Change Path", self)

        self.path_edit.clicked.connect(self.change_value)
        
        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0)
        self.layout.addWidget(self.path_edit, 1, 0)
        self.setLayout(self.layout)
    
    def change_value(self):
        fileName = QFileDialog.getOpenFileName(
            self,
            "Open "+self.component.type.split(" ")[0],
            self.component.path,
            self.component.type
        )
        if len(fileName[0]) > 0:
            self.component.path = fileName[0]
            self.parent.parent.project.save()
            self.parent.parent.assets_explorer.open_folder(self.parent.parent.assets_explorer.current_folder)
            self.parent.parent.viewport.update_screen()
