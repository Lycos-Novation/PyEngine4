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
        self.delete_btn = QPushButton("Delete", self)
        self.script_edit = QPushButton("Change Script", self)
        self.script_edit.clicked.connect(self.change_value)
        self.delete_btn.clicked.connect(self.delete)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 1, 1, 3)
        self.layout.addWidget(self.delete_btn, 0, 4)
        self.layout.addWidget(self.script_edit, 1, 0, 1, 5)
        self.setLayout(self.layout)

    def delete(self):
        self.parent.remove_component(self.component.name)

    def dragEnterEvent(self, e) -> None:
        if e.mimeData().hasFormat("assets/script"):
            e.accept()
        else:
            super().dragEnterEvent(e)

    def dragMoveEvent(self, e) -> None:
        if e.mimeData().hasFormat("assets/script"):
            e.setDropAction(Qt.CopyAction)
            e.accept()
        else:
            super().dragMoveEvent(e)

    def dropEvent(self, e) -> None:
        if e.mimeData().hasFormat("assets/script"):
            data = str(e.mimeData().data("assets/script"), "utf-8")
            self.change_script(data)
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
