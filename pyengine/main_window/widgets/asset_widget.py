from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

from pyengine.common.utils import core_logger


class AssetWidget(QWidget):
    def __init__(self, parent, path, name, icon):
        super().__init__(parent)
        self.path = path
        self.title = QLabel(name.replace(".json", "").replace(".py", ""))
        self.title.setFont(QFont("arial", 16))
        self.title.setAlignment(Qt.AlignHCenter)
        self.icon = QLabel("")
        self.icon.setAlignment(Qt.AlignHCenter)

        pix = QPixmap()
        if pix.load(icon):
            self.icon.setPixmap(pix.scaled(64, 64, Qt.KeepAspectRatio))
        else:
            core_logger.error("AssetWidget : Cannot load " + icon)
        
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.icon)
        self.layout.addWidget(self.title)

        self.setLayout(self.layout)
