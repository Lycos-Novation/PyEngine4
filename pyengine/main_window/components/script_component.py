from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QGridLayout, QFileDialog
from PyQt5.QtCore import Qt

import os


class ScriptComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component
        self.setAcceptDrops(True)

        comp_name = self.component.name.split(" ")[-1] if len(self.component.name.split(" ")[-1]) > 0 else "None"
        self.name = QLabel("Script : " + comp_name, self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.script_edit = QPushButton("Change Script", self)
        self.script_edit.clicked.connect(self.change_value)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0)
        self.layout.addWidget(self.script_edit, 1, 0)
        self.setLayout(self.layout)

    def dragEnterEvent(self, e) -> None:
        if e.mimeData().hasFormat("pe4/asset"):
            e.accept()
        else:
            super().dragEnterEvent(e)

    def dragMoveEvent(self, e) -> None:
        if e.mimeData().hasFormat("pe4/asset"):
            e.setDropAction(Qt.CopyAction)
            e.accept()
        else:
            super().dragMoveEvent(e)

    def dropEvent(self, e) -> None:
        if e.mimeData().hasFormat("pe4/asset"):
            datas = str(e.mimeData().data("pe4/asset"), "utf-8").split("-")
            if len(datas) == 2:
                if os.path.basename(datas[0]) == "scripts":
                    self.change_script(datas[1])
                    e.accept()
                    return
        super().dropEvent(e)

    def change_value(self):
        file_name = QFileDialog.getOpenFileName(
            self,
            "Open Script",
            self.parent.parent.project.folders["scripts"],
            "Scripts (*.py)"
        )
        if len(file_name[0]) > 0:
            self.change_script(file_name[0])

    def change_script(self, file):
        self.component.name = "ScriptComponent " + os.path.basename(file.replace(".py", ""))
        comp_name = self.component.name.split(" ")[-1] if len(self.component.name.split(" ")[-1]) > 0 else "None"
        self.name.setText("Script : " + comp_name)
        self.parent.parent.project.save()
        self.parent.parent.viewport.update_screen()
