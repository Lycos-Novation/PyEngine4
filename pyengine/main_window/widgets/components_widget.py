from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QListWidgetItem, QMenu, QAction, \
    QAbstractItemView
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
        self.add_component = QPushButton("Add Component", self)

        self.title.setFont(QFont("arial", 18, 1, False))
        self.title.setAlignment(Qt.AlignHCenter)
        self.list_components.setContextMenuPolicy(Qt.CustomContextMenu)
        self.list_components.setSelectionMode(QAbstractItemView.SingleSelection)
        self.add_component.setEnabled(False)

        self.add_component.clicked.connect(self.add)
        self.list_components.customContextMenuRequested.connect(self.components_context_menu)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.list_components)
        self.layout.addWidget(self.add_component)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

    def components_context_menu(self):
        menu = QMenu(self)
        create_transform = QAction("Transform", self)
        create_transform.triggered.connect(lambda: self.create_component("TransformComponent"))
        create_sprite = QAction("Sprite", self)
        create_sprite.triggered.connect(lambda: self.create_component("SpriteComponent"))
        create_text = QAction("Text", self)
        create_text.triggered.connect(lambda: self.create_component("TextComponent"))
        create_collision = QAction("Collision", self)
        create_collision.triggered.connect(lambda: self.create_component("CollisionComponent"))
        create_phys = QAction("Basic Physics", self)
        create_phys.triggered.connect(lambda: self.create_component("BasicPhysicComponent"))
        create_control = QAction("Control", self)
        create_control.triggered.connect(lambda: self.create_component("ControlComponent"))
        create_spritesheet = QAction("SpriteSheet", self)
        create_spritesheet.triggered.connect(lambda: self.create_component("SpriteSheetComponent"))
        create_script = QAction("Script", self)
        create_script.triggered.connect(lambda: self.create_component("ScriptComponent"))
        menu.addActions([
            create_transform,
            create_sprite,
            create_text,
            create_collision,
            create_phys,
            create_control,
            create_spritesheet,
            create_script
        ])
        if len(self.list_components.selectedItems()) >= 1:
            widget = self.list_components.itemWidget(self.list_components.selectedItems()[0])
            remove = QAction("Delete Component", self)
            remove.triggered.connect(lambda: self.remove_component(widget.component.name))
            menu.addAction(remove)
        menu.exec_(QCursor.pos())

    def add(self):
        menu = QMenu(self)
        create_transform = QAction("Transform", self)
        create_transform.triggered.connect(lambda: self.create_component("TransformComponent"))
        create_sprite = QAction("Sprite", self)
        create_sprite.triggered.connect(lambda: self.create_component("SpriteComponent"))
        create_text = QAction("Text", self)
        create_text.triggered.connect(lambda: self.create_component("TextComponent"))
        create_collision = QAction("Collision", self)
        create_collision.triggered.connect(lambda: self.create_component("CollisionComponent"))
        create_phys = QAction("Basic Physics", self)
        create_phys.triggered.connect(lambda: self.create_component("BasicPhysicComponent"))
        create_control = QAction("Control", self)
        create_control.triggered.connect(lambda: self.create_component("ControlComponent"))
        create_spritesheet = QAction("SpriteSheet", self)
        create_spritesheet.triggered.connect(lambda: self.create_component("SpriteSheetComponent"))
        create_script = QAction("Script", self)
        create_script.triggered.connect(lambda: self.create_component("ScriptComponent"))
        menu.addActions([
            create_transform,
            create_sprite,
            create_text,
            create_collision,
            create_phys,
            create_control,
            create_spritesheet,
            create_script
        ])
        menu.exec_(QCursor.pos())

    def remove_component(self, comp):
        self.obj.components.remove(self.obj.get_component(comp))
        self.set_obj(self.obj)
        self.parent.project.save()
        self.parent.viewport.update_screen()

    def create_component(self, comp):
        if comp == "TransformComponent":
            self.obj.components.append(components.TransformComponent())
        elif comp == "SpriteComponent":
            self.obj.components.append(components.SpriteComponent())
        elif comp == "TextComponent":
            self.obj.components.append(components.TextComponent())
        elif comp == "ScriptComponent":
            self.obj.components.append(components.ScriptComponent())
        elif comp == "CollisionComponent":
            self.obj.components.append(components.CollisionComponent())
        elif comp == "BasicPhysicComponent":
            self.obj.components.append(components.BasicPhysicComponent())
        elif comp == "ControlComponent":
            self.obj.components.append(components.ControlComponent())
        elif comp == "SpriteSheetComponent":
            self.obj.components.append(components.SpriteSheetComponent())
        self.set_obj(self.obj)
        self.parent.project.save()
        self.parent.viewport.update_screen()

    def set_obj(self, obj):
        self.obj = obj
        self.title.setText(obj.name.replace("_", " ").title())
        if obj.__class__ == GameObject:
            self.add_component.setEnabled(True)
        else:
            self.add_component.setEnabled(False)
        self.list_components.clear()
        for i in self.obj.components:
            w = None
            if i.name == "ColorComponent":
                w = ColorComponent(self, i)
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
            elif i.name.startswith("ScriptComponent"):
                w = ScriptComponent(self, i)
            else:
                continue
            wi = QListWidgetItem()
            wi.setSizeHint(w.sizeHint())
            self.list_components.addItem(wi)
            self.list_components.setItemWidget(wi, w)
