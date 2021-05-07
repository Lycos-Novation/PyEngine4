from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QListWidgetItem, QMenu, QAction, \
    QAbstractItemView, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt

from pyengine.main_window.components import *
from pyengine.common import components
from pyengine.common.project_objects import GameObject


class ComponentsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.obj = None

        self.title = QLabel("None", self)
        self.list_components = QListWidget(self)
        self.add_component = QPushButton("Add", self)
        self.del_component = QPushButton("Remove", self)

        self.title.setFont(QFont("arial", 18, 1, False))
        self.add_component.setFont(QFont("arial", 18))
        self.del_component.setFont(QFont("arial", 18))
        self.title.setAlignment(Qt.AlignHCenter)
        self.list_components.setContextMenuPolicy(Qt.CustomContextMenu)
        self.list_components.setSelectionMode(QAbstractItemView.SingleSelection)
        self.add_component.setEnabled(False)
        self.del_component.setEnabled(False)

        self.add_component.clicked.connect(self.add)
        self.del_component.clicked.connect(self.remove_component)
        self.list_components.itemClicked.connect(self.select_component)
        self.list_components.customContextMenuRequested.connect(self.components_context_menu)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.list_components)
        internal_layout = QHBoxLayout(self)
        internal_layout.addWidget(self.add_component)
        internal_layout.addWidget(self.del_component)
        self.layout.addLayout(internal_layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

    def select_component(self):
        if len(self.list_components.selectedItems()) >= 1:
            widget = self.list_components.itemWidget(self.list_components.selectedItems()[0])
            if not isinstance(widget, TagComponent) and not isinstance(widget, TimeScaleComponent) and \
                    widget.component.name not in ("ColorComponent", "PathComponent"):
                self.del_component.setEnabled(True)
            else:
                self.del_component.setEnabled(False)
        else:
            self.del_component.setEnabled(False)

    def components_context_menu(self):
        if self.obj.__class__ == GameObject:
            menu = QMenu(self)
            for i in (
                "Transform", "Sprite", "Text", "Collision", "BasicPhysic", "Control", "SpriteSheet", "Auto", "Button",
                "Music", "Sound", "Anim", "Script"
            ):
                action = QAction(i, self)
                action.triggered.connect(lambda _, comp=i: self.create_component(comp + "Component"))
                menu.addAction(action)
            if len(self.list_components.selectedItems()) >= 1:
                widget = self.list_components.itemWidget(self.list_components.selectedItems()[0])
                if widget.component.name not in ("ColorComponent", "PathComponent"):
                    menu.addSeparator()
                    remove = QAction("Delete Component", self)
                    remove.triggered.connect(lambda: self.remove_component(comp=widget.component.name))
                    menu.addAction(remove)
            menu.exec_(QCursor.pos())

    def add(self):
        menu = QMenu(self)
        for i in (
            "Transform", "Sprite", "Text", "Collision", "BasicPhysic", "Control", "SpriteSheet", "Auto", "Button",
            "Music", "Sound", "Anim", "Script"
        ):
            action = QAction(i, self)
            action.triggered.connect(lambda _, comp=i: self.create_component(comp + "Component"))
            menu.addAction(action)
        menu.exec_(QCursor.pos())

    def remove_component(self, _=None, comp=None):
        if comp is None:
            if len(self.list_components.selectedItems()) >= 1:
                widget = self.list_components.itemWidget(self.list_components.selectedItems()[0])
                if widget.component.name not in ("ColorComponent", "PathComponent", "TimeScaleComponent", "TagComponent"):
                    self.remove_component(comp=widget.component.name)
            return
        self.obj.components.remove(self.obj.get_component(comp))
        self.set_obj(self.obj)
        self.parent.project.save()
        self.parent.viewport.update_screen()

    def create_component(self, comp):
        if self.obj.get_component(comp) is not None:
            QMessageBox.warning(self, "PyEngine4 - Adding Component", "The object already have this kind of component.")
            return
        if comp == "TransformComponent":
            self.obj.components.append(components.TransformComponent(self.obj))
        elif comp == "SpriteComponent":
            self.obj.components.append(components.SpriteComponent(self.obj))
        elif comp == "TextComponent":
            self.obj.components.append(components.TextComponent(self.obj))
        elif comp == "ScriptComponent":
            self.obj.components.append(components.ScriptComponent(self.obj))
        elif comp == "CollisionComponent":
            self.obj.components.append(components.CollisionComponent(self.obj))
        elif comp == "BasicPhysicComponent":
            self.obj.components.append(components.BasicPhysicComponent(self.obj))
        elif comp == "ControlComponent":
            self.obj.components.append(components.ControlComponent(self.obj))
        elif comp == "SpriteSheetComponent":
            self.obj.components.append(components.SpriteSheetComponent(self.obj))
        elif comp == "ButtonComponent":
            self.obj.components.append(components.ButtonComponent(self.obj))
        elif comp == "AutoComponent":
            self.obj.components.append(components.AutoComponent(self.obj))
        elif comp == "SoundComponent":
            self.obj.components.append(components.SoundComponent(self.obj))
        elif comp == "MusicComponent":
            self.obj.components.append(components.MusicComponent(self.obj))
        elif comp == "AnimComponent":
            self.obj.components.append(components.AnimComponent(self.obj))
        self.set_obj(self.obj)
        self.parent.project.save()
        self.parent.viewport.update_screen()

    def set_obj(self, obj):
        self.obj = obj
        self.title.setText(obj.name.replace("_", " ").title())
        self.list_components.clear()
        self.del_component.setEnabled(False)
        if obj.__class__ == GameObject:
            self.add_component.setEnabled(True)
            w = TagComponent(self, obj)
            wi = QListWidgetItem()
            wi.setSizeHint(w.sizeHint())
            self.list_components.addItem(wi)
            self.list_components.setItemWidget(wi, w)
        else:
            self.add_component.setEnabled(False)
        for i in self.obj.components:
            w = None
            if i.name == "ColorComponent":
                w = ColorComponent(self, i)
            elif i.name == "TimeScaleComponent":
                w = TimeScaleComponent(self, i)
            elif i.name == "TransformComponent":
                w = TransformComponent(self, i)
            elif i.name == "PathComponent":
                w = PathComponent(self, i)
            elif i.name == "SpriteComponent":
                w = SpriteComponent(self, i)
            elif i.name == "TextComponent":
                w = TextComponent(self, i)
            elif i.name == "CollisionComponent":
                w = CollisionComponent(self, i)
            elif i.name == "BasicPhysicComponent":
                w = BasicPhysicComponent(self, i)
            elif i.name == "ControlComponent":
                w = ControlComponent(self, i)
            elif i.name == "SpriteSheetComponent":
                w = SpriteSheetComponent(self, i)
            elif i.name == "AutoComponent":
                w = AutoComponent(self, i)
            elif i.name == "ButtonComponent":
                w = ButtonComponent(self, i)
            elif i.name == "MusicComponent":
                w = MusicComponent(self, i)
            elif i.name == "SoundComponent":
                w = SoundComponent(self, i)
            elif i.name == "AnimComponent":
                w = AnimComponent(self, i)
            elif i.name.startswith("ScriptComponent"):
                w = ScriptComponent(self, i)
            else:
                continue
            wi = QListWidgetItem()
            wi.setSizeHint(w.sizeHint())
            self.list_components.addItem(wi)
            self.list_components.setItemWidget(wi, w)
