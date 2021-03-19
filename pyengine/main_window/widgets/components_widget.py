from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QListWidget, QPushButton, QListWidgetItem, QMenu, QAction
from PyQt5.QtGui import QFont, QCursor
from PyQt5.QtCore import Qt

from pyengine.main_window.components import *
from pyengine.common import components
from pyengine.common.project_objects import Entity


class ComponentsWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.obj = None

        self.title = QLabel("None", self)
        self.title.setFont(QFont("arial", 18, 1, False))
        self.title.setAlignment(Qt.AlignHCenter)
        self.list_components = QListWidget(self)
        self.add_component = QPushButton("Add Component", self)
        self.add_component.setEnabled(False)

        self.add_component.clicked.connect(self.add)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.list_components)
        self.layout.addWidget(self.add_component)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.setLayout(self.layout)

    def add(self):
        menu = QMenu(self)
        create_transform = QAction("Transform", self)
        create_transform.triggered.connect(lambda: self.create_component("TransformComponent"))
        menu.addAction(create_transform)
        create_sprite = QAction("Sprite", self)
        create_sprite.triggered.connect(lambda: self.create_component("SpriteComponent"))
        menu.addAction(create_sprite)
        menu.exec_(QCursor.pos())
    
    def create_component(self, comp):
        if comp == "TransformComponent":
            self.obj.components.append(components.TransformComponent())
            self.set_obj(self.obj)
            self.parent.project.save()
            self.parent.viewport.update_screen()
        elif comp == "SpriteComponent":
            self.obj.components.append(components.SpriteComponent())
            self.set_obj(self.obj)
            self.parent.project.save()
            self.parent.viewport.update_screen()

    def set_obj(self, obj):
        self.obj = obj
        self.title.setText(obj.name.replace("_", " ").title())
        if obj.__class__ == Entity:
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
            else:
                continue
            wi = QListWidgetItem()
            wi.setSizeHint(w.sizeHint())
            self.list_components.addItem(wi)
            self.list_components.setItemWidget(wi, w)
