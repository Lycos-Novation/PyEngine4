from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

import os


class ProjectAbstract(QWidget):
    def __init__(self, parent, project):
        super().__init__(parent)
        self.project = project
        self.title = QLabel(project.name)
        self.title.setFont(QFont("arial", 25, 2, False))
        self.author = QLabel(project.author)
        self.author.setFont(QFont("arial", 18, 1, False))
        self.icon = QLabel("")
        self.icon.setAlignment(Qt.AlignHCenter)

        pix = QPixmap()
        if pix.load(os.path.join("pyengine", "resources", "icon.png") if project.icon == "default" else project.icon):
            self.icon.setPixmap(pix.scaled(128, 128, Qt.KeepAspectRatio))
        else:
            print(
                "ERROR : Cannot load",
                os.path.join("pyengine", "resources", "icon.png") if project.icon == "default" else project.icon
            )
        
        self.layout = QGridLayout()

        self.layout.addWidget(self.icon, 0, 0, 2, 1)
        self.layout.addWidget(self.title, 0, 1)
        self.layout.addWidget(self.author, 1, 1)

        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 2)

        self.setLayout(self.layout)
