from PyQt5.QtWidgets import QWidget, QGridLayout, QMenuBar, QAction
from PyQt5.QtCore import Qt

from pyengine.main_window.widgets import *


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.project = None

        self.viewport = Viewport(self)
        self.scene_tree = SceneTree(self)
        self.assets_explorer = AssetsExplorer(self)
        self.components = ComponentsWidget(self)
        self.settings = Settings(self)

        self.menu_bar = QMenuBar(self)
        project_menu = self.menu_bar.addMenu("Project")
        project_build = QAction('Build', self)
        project_build.triggered.connect(self.build_project)
        project_launch = QAction("Launch", self)
        project_launch.triggered.connect(self.launch_project)
        project_build_launch = QAction("Build and Launch", self)
        project_build_launch.triggered.connect(self.build_launch_project)
        project_menu.addActions([project_build, project_launch, project_build_launch])
        project_menu.addSeparator()
        project_settings = QAction("Settings", self)
        project_settings.triggered.connect(self.open_settings)
        project_menu.addAction(project_settings)

        self.layout = QGridLayout()
        self.layout.addWidget(self.menu_bar, 0, 0, 1, 3)
        self.layout.addWidget(self.scene_tree, 1, 0)
        self.layout.addWidget(self.viewport, 1, 1)
        self.layout.addWidget(self.assets_explorer, 2, 0, 1, 2)
        self.layout.addWidget(self.components, 1, 2, 2, 1)
        self.layout.setColumnStretch(0, 1)
        self.layout.setColumnStretch(1, 2)
        self.layout.setColumnStretch(2, 1)
        self.layout.setRowStretch(1, 2)
        self.layout.setRowStretch(2, 1)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.setLayout(self.layout)
    
    def build_launch_project(self):
        self.build_project()
        self.launch_project()
    
    def launch_project(self):
        if self.project is not None:
            self.showMinimized()
            self.project.launch()
            self.showMaximized()

    def build_project(self):
        if self.project is not None:
            self.project.build()

    def open_settings(self):
        if self.project is not None:
            self.settings.set_project(self.project)
            self.settings.setWindowModality(Qt.ApplicationModal)
            self.settings.show()

    def set_project(self, project):
        self.project = project
        self.setWindowTitle("PyEngine4 - "+project.name)
        self.assets_explorer.update_project()
        self.viewport.update_screen()
        main_scene = self.project.settings.get("mainScene", None)
        if main_scene is not None and self.project.get_scene(main_scene) is not None:
            self.scene_tree.update_scene(self.project.get_scene(main_scene))
