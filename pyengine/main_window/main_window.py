from PyQt5.QtWidgets import QWidget, QGridLayout, QMenuBar, QAction, QMessageBox
from PyQt5.QtCore import Qt

from pyengine.main_window.widgets import *
from pyengine.common import EngineSettings

import webbrowser


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.project = None

        self.engine_settings = EngineSettings()
        self.viewport = Viewport(self)
        self.scene_tree = SceneTree(self)
        self.assets_explorer = AssetsExplorer(self)
        self.components = ComponentsWidget(self)
        self.settings = Settings(self)
        self.pysettings = PySettings(self)
        self.about = About(self)

        self.menu_bar = QMenuBar(self)
        self.setup_menu_bar()

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

    def setup_menu_bar(self):
        project_menu = self.menu_bar.addMenu("Project")
        project_build = QAction('Build', self)
        project_build.triggered.connect(self.build_project)
        project_launch = QAction("Launch", self)
        project_launch.triggered.connect(self.launch_project)
        project_build_launch = QAction("Build and Launch", self)
        project_build_launch.triggered.connect(self.build_launch_project)
        project_menu.addActions([project_build, project_launch, project_build_launch])
        project_menu.addSeparator()
        project_settings = QAction("Project Settings", self)
        project_settings.triggered.connect(self.open_settings)
        project_menu.addAction(project_settings)

        help_menu = self.menu_bar.addMenu("Engine")
        engine_settings = QAction("Engine Settings", self)
        engine_settings.triggered.connect(self.open_pysettings)
        help_menu.addAction(engine_settings)
        help_menu.addSeparator()
        help_doc = QAction('Docs', self)
        help_doc.triggered.connect(lambda: webbrowser.open("https://pyengine4-docs.readthedocs.io/en/latest/"))
        help_about = QAction('About', self)
        help_about.triggered.connect(self.open_about)
        help_menu.addActions([help_doc, help_about])
    
    def build_launch_project(self):
        self.build_project()
        self.launch_project()
    
    def launch_project(self):
        if self.project is not None:
            self.showMinimized()
            if self.project.launch():
                QMessageBox.warning(self, "Launching Error", "Launching Game make an error.\nSee logs.")
            self.showMaximized()

    def build_project(self):
        if self.project is not None:
            self.project.build()

    def open_settings(self):
        if self.project is not None:
            self.settings.set_project(self.project)
            self.settings.setWindowModality(Qt.ApplicationModal)
            self.settings.show()

    def open_about(self):
        self.about.setWindowModality(Qt.ApplicationModal)
        self.about.show()

    def open_pysettings(self):
        self.pysettings.setWindowModality(Qt.ApplicationModal)
        self.pysettings.show()

    def set_project(self, project):
        self.project = project
        self.setWindowTitle("PyEngine4 - "+project.name)
        self.assets_explorer.update_project()
        self.viewport.update_screen()
        main_scene = self.project.settings.get("mainScene", None)
        if main_scene is not None and self.project.get_scene(main_scene) is not None:
            self.scene_tree.update_scene(self.project.get_scene(main_scene))
