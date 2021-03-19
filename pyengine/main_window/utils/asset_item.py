from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtGui import QFont


class AssetItem(QListWidgetItem):
    def __init__(self, name, folder):
        super().__init__(name)
        self.folder = folder
        self.setFont(QFont("arial", 16))
