from PyQt5.QtWidgets import QListWidget, QAbstractItemView
from PyQt5.QtCore import Qt, QMimeData
from PyQt5.QtGui import QDragMoveEvent, QDrag

import os


class ContentFolder(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setViewMode(QListWidget.IconMode)
        self.setDragEnabled(True)
        self.setContextMenuPolicy(Qt.CustomContextMenu)

    def dragMoveEvent(self, e: QDragMoveEvent) -> None:
        if e.mimeData().hasFormat("pe4/asset"):
            e.setDropAction(Qt.MoveAction)
            e.accept()
        else:
            e.ignore()

    def startDrag(self, supported_actions) -> None:
        widget = self.itemWidget(self.selectedItems()[0])

        mimeData = QMimeData()
        folder = os.path.basename(self.parent.current_folder)
        if folder == "scripts":
            mimeData.setData("assets/script", widget.path.encode("utf-8"))
        elif folder == "textures":
            mimeData.setData("assets/texture", widget.path.encode("utf-8"))
        else:
            return

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(widget.icon.pixmap())
        drag.exec(Qt.MoveAction)
