from PyQt5.QtWidgets import QWidget, QListWidget, QHBoxLayout, QAbstractItemView, QListWidgetItem, QMenu, QAction, \
    QInputDialog, QLineEdit, QFileDialog, QPushButton, QSizePolicy
from PyQt5.QtGui import QCursor, QFont

from pyengine.main_window.utils import AssetItem
from pyengine.main_window.widgets.asset_widget import AssetWidget
from pyengine.main_window.widgets.content_folder import ContentFolder
from pyengine.common.project_objects import *

import os
import subprocess


class AssetsExplorer(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.list_folder = QListWidget(self)
        self.list_folder.setSelectionMode(QAbstractItemView.SingleSelection)
        self.current_folder = None
        self.folders = {}
        self.content_folder = ContentFolder(self)
        self.add_asset = QPushButton("+", self)
        self.add_asset.setFont(QFont("arial", 18))
        self.add_asset.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.add_asset.clicked.connect(self.context_menu_folder)
        self.list_folder.itemClicked.connect(self.select_folder)
        self.content_folder.itemDoubleClicked.connect(self.open_content)
        self.content_folder.customContextMenuRequested.connect(self.context_menu_folder)

        self.layout = QHBoxLayout()
        self.layout.addWidget(self.list_folder, 3)
        self.layout.addWidget(self.content_folder, 20)
        self.layout.addWidget(self.add_asset, 1)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        self.setLayout(self.layout)

    def context_menu_folder(self):
        if self.current_folder == self.folders["scenes"]:
            menu = QMenu(self.content_folder)
            create_scene = QAction("Create Scene", self)
            create_scene.triggered.connect(lambda: self.create_asset("scene"))
            menu.addAction(create_scene)
            if len(self.content_folder.selectedItems()) >= 1:
                widget = self.content_folder.itemWidget(self.content_folder.selectedItems()[0])
                remove_scene = QAction("Delete Scene", self)
                remove_scene.triggered.connect(lambda: self.remove_asset("scene", widget.title.text()))
                menu.addAction(remove_scene)
            menu.exec_(QCursor.pos())
        elif self.current_folder == self.folders["textures"]:
            menu = QMenu(self.content_folder)
            create_texture = QAction("Import Texture", self)
            create_texture.triggered.connect(lambda: self.create_asset("texture"))
            menu.addAction(create_texture)
            if len(self.content_folder.selectedItems()) >= 1:
                widget = self.content_folder.itemWidget(self.content_folder.selectedItems()[0])
                remove_texture = QAction("Delete Texture", self)
                remove_texture.triggered.connect(lambda: self.remove_asset("texture", widget.title.text()))
                menu.addAction(remove_texture)
            menu.exec_(QCursor.pos())
        elif self.current_folder == self.folders["sounds"]:
            menu = QMenu(self.content_folder)
            create_sound = QAction("Import Sound", self)
            create_sound.triggered.connect(lambda: self.create_asset("sound"))
            menu.addAction(create_sound)
            if len(self.content_folder.selectedItems()) >= 1:
                widget = self.content_folder.itemWidget(self.content_folder.selectedItems()[0])
                remove_sound = QAction("Delete Sound", self)
                remove_sound.triggered.connect(lambda: self.remove_asset("sound", widget.title.text()))
                menu.addAction(remove_sound)
            menu.exec_(QCursor.pos())
        elif self.current_folder == self.folders["scripts"]:
            menu = QMenu(self.content_folder)
            create_script = QAction("Create Script", self)
            create_script.triggered.connect(lambda: self.create_asset("script"))
            menu.addAction(create_script)
            if len(self.content_folder.selectedItems()) >= 1:
                widget = self.content_folder.itemWidget(self.content_folder.selectedItems()[0])
                remove_script = QAction("Delete Script", self)
                remove_script.triggered.connect(lambda: self.remove_asset("script", widget.title.text()))
                menu.addAction(remove_script)
            menu.exec_(QCursor.pos())

    def select_folder(self):
        if len(self.list_folder.selectedItems()) >= 1:
            folder = self.list_folder.selectedItems()[0].folder
            self.open_folder(folder)
        
    def open_content(self):
        if len(self.content_folder.selectedItems()) >= 1:
            widget = self.content_folder.itemWidget(self.content_folder.selectedItems()[0])
            if os.path.isdir(widget.path):
                self.open_folder(widget.path)
            elif self.current_folder == self.folders["scenes"]:
                self.parent.scene_tree.update_scene(self.parent.project.get_scene(widget.title.text()))
            elif self.current_folder == self.folders["textures"]:
                self.parent.components.set_obj(self.parent.project.get_texture(widget.title.text()))
            elif self.current_folder == self.folders["sounds"]:
                self.parent.components.set_obj(self.parent.project.get_sound(widget.title.text()))
            elif self.current_folder == self.folders["scripts"]:
                self.open_script(widget.title.text())
    
    def open_script(self, name):
        editor = self.parent.engine_settings.values.get("editor", None)
        if editor is not None:
            path = os.path.abspath(os.path.join(self.parent.project.folders["scripts"], name+".py"))
            subprocess.Popen([editor, path], cwd=editor.split("\\")[0].split("/")[0])

    def open_folder(self, folder):
        self.current_folder = folder
        self.content_folder.clear()
        for i in os.listdir(folder):
            if os.path.isdir(os.path.join(folder, i)):
                icon = os.path.join("pyengine", "resources", "folder.png")
            elif self.current_folder == self.folders["textures"]:
                icon = self.parent.project.get_texture(i.replace(".json", "")).components[0].path
            elif self.current_folder == self.folders["sounds"]:
                icon = os.path.join("pyengine", "resources", "sound.png")
            else:
                icon = os.path.join("pyengine", "resources", "file.png")
            
            w = AssetWidget(self, os.path.join(folder, i), i, icon)
            wi = QListWidgetItem()
            wi.setSizeHint(w.sizeHint())
            self.content_folder.addItem(wi)
            self.content_folder.setItemWidget(wi, w)

    def update_project(self):
        self.list_folder.clear()
        for k, v in self.parent.project.folders.items():
            if k != "assets" and k != "main":
                self.folders[k] = v
                self.list_folder.addItem(AssetItem(k.capitalize(), v))

        self.list_folder.setCurrentRow(0)
        self.open_folder(self.list_folder.item(0).folder)

    def create_asset(self, asset):
        if asset == "scene":
            text = QInputDialog.getText(self, "PyEngine4 - Create Scene", "Scene Name:", QLineEdit.Normal)
            if text[1] and len(text[0]) > 0:
                self.parent.project.scenes.append(Scene(text[0]))
                self.parent.project.save()
                self.open_folder(self.current_folder)
        elif asset == "texture":
            name = QInputDialog.getText(self, "PyEngine4 - Import Texture", "Texture Name:", QLineEdit.Normal)
            if len(name[0]) == 0:
                return
            fileName = QFileDialog.getOpenFileName(self, "Open Image", filter="Image (*.png *.jpg)")
            if len(fileName[0]) > 0:
                self.parent.project.textures.append(Texture(name[0], fileName[0]))
                self.parent.project.save()
                self.open_folder(self.current_folder)
        elif asset == "sound":
            name = QInputDialog.getText(self, "PyEngine4 - Import Sound", "Sound Name:", QLineEdit.Normal)
            if len(name[0]) == 0:
                return
            fileName = QFileDialog.getOpenFileName(self, "Open Sound", filter="Sound (*.ogg *.wav *.mp3)")
            if len(fileName[0]) > 0:
                self.parent.project.sounds.append(Sound(name[0], fileName[0]))
                self.parent.project.save()
                self.open_folder(self.current_folder)
        elif asset == "script":
            name = QInputDialog.getText(self, "PyEngine4 - Create Script", "Script Name:", QLineEdit.Normal)
            if len(name[0]) == 0:
                return
            self.parent.project.scripts.append(name[0])
            with open(os.path.join(self.parent.project.folders["scripts"], name[0]+".py"), "w") as f:
                f.write(
                    f"from files.scripts.script import Script\n\n\n"
                    f"class {name[0].title()}(Script):\n"
                    f"    def __init__(self, engine):\n"
                    f"        super().__init__(engine, \"{name[0]}\")\n"
                )
            self.open_script(name[0])
            self.open_folder(self.current_folder)
    
    def remove_asset(self, asset, name):
        if asset == "texture":
            self.parent.project.textures.remove(self.parent.project.get_texture(name))
            self.parent.project.save()
            self.open_folder(self.current_folder)
        elif asset == "sound":
            self.parent.project.sounds.remove(self.parent.project.get_sound(name))
            self.parent.project.save()
            self.open_folder(self.current_folder)
        elif asset == "scene":
            self.parent.project.scenes.remove(self.parent.project.get_scene(name))
            self.parent.project.save()
            self.open_folder(self.current_folder)
        elif asset == "script":
            self.parent.project.scripts.remove(name)
            os.remove(os.path.join(self.parent.project.folders["scripts"], name+".py"))
            self.open_folder(self.current_folder)
