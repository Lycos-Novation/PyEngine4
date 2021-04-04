from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QLabel, QMessageBox, QFileDialog

import shutil
import os

from pyengine.project_window.project_manager import ProjectManager
from pyengine.project_window.widgets import ProjectList
from pyengine.main_window.main_window import MainWindow
from pyengine import common


class ProjectWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.main = MainWindow()
        
        self.setWindowTitle('PyEngine4 - Projects')
        self.resize(800, 450)
        
        self.project_manager = ProjectManager()
        self.project_manager.load_projects()

        self.project_list = ProjectList(self, self.project_manager.projects)
        self.project_name = QLineEdit("Unknown Project", self)
        self.project_author = QLineEdit("Unknown Author", self)
        self.project_icon = "default"
        self.icon_button = QPushButton("Select Icon", self)
        self.add_project_button = QPushButton("Create Project", self)
        self.remove_project_button = QPushButton("Remove Project", self)

        self.add_project_button.clicked.connect(self.add_project)
        self.remove_project_button.clicked.connect(self.remove_project)
        self.icon_button.clicked.connect(self.select_icon)
        self.project_list.itemDoubleClicked.connect(self.open_mainwindow)

        self.layout = QHBoxLayout()
        internal_layout = QVBoxLayout()
        internal_layout.addWidget(QLabel("Name :"))
        internal_layout.addWidget(self.project_name)
        internal_layout.addSpacing(20)
        internal_layout.addWidget(QLabel("Author :"))
        internal_layout.addWidget(self.project_author)
        internal_layout.addSpacing(20)
        internal_layout.addWidget(QLabel("Icon :"))
        internal_layout.addWidget(self.icon_button)
        internal_layout.addSpacing(30)
        internal_layout.addWidget(self.add_project_button)
        internal_layout.addSpacing(10)
        internal_layout.addWidget(self.remove_project_button)
        internal_layout.addStretch()
        self.layout.addWidget(self.project_list, 2)
        self.layout.addLayout(internal_layout, 1)
    
        self.setLayout(self.layout)

    def open_mainwindow(self):
        if len(self.project_list.selectedItems()) >= 1:
            project = self.project_list.itemWidget(self.project_list.selectedItems()[0]).project
            if common.__version__ != project.settings.get("engine_version", ""):
                if QMessageBox.question(
                    self,
                    "PyEngine4 - Launch Project",
                    "This project use a different version of PyEngine4.\nDo you want to load it anyway ?"
                ) == QMessageBox.StandardButton.No:
                    return
            project.save()
            self.main.set_project(project)
            self.main.showMaximized()
            self.close()

    def select_icon(self):
        file_name = QFileDialog.getOpenFileName(self, "Open Icon", filter="Icons (*.png *.jpg)")
        if file_name[0] == "":
            self.project_icon = "default"
        else:
            self.project_icon = file_name[0]

    def add_project(self):
        if self.project_name.text() == "":
            QMessageBox.warning(self, "PyEngine4 - Create Project", "Enter a name for the project.")
            return
        if self.project_author.text() == "":
            QMessageBox.warning(self, "PyEngine4 - Create Project", "Enter an author for the project.")
            return
        if self.project_icon == "":
            QMessageBox.warning(self, "PyEngine4 - Create Project", "Enter an icon for the project.")
            return

        if self.project_manager.exist(self.project_name.text()):
            QMessageBox.warning(self, "PyEngine4 - Create Project", "This name is already taken.")
            return

        self.project_manager.create_project(self.project_name.text(), self.project_author.text(), self.project_icon)
        self.project_list.update_list(self.project_manager.projects)
        for i in self.project_manager.projects:
            if common.__version__ == i.settings.get("engine_version", ""):
                i.save()
    
    def remove_project(self):
        if len(self.project_list.selectedItems()) >= 1:
            project = self.project_list.itemWidget(self.project_list.selectedItems()[0]).project
            msg = QMessageBox()
            msg.setWindowTitle("PyEngine4 - Delete Project")
            msg.setText("Are you sure you want to delete '"+project.name+"'?")
            msg.setInformativeText("The files will also be deleted from your computer.")
            msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.Cancel)
            ret = msg.exec()
            if ret == QMessageBox.StandardButton.Yes:
                self.project_manager.projects.remove(project)
                self.project_list.update_list(self.project_manager.projects)
                shutil.rmtree(os.path.join("projects", project.name))
