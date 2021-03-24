from PyQt5.QtWidgets import QTreeWidget, QMessageBox, QAction, QMenu, QInputDialog, QLineEdit
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt

from pyengine.main_window.utils import GameObjectItem
from pyengine.common.project_objects import GameObject


class SceneTree(QTreeWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.scene = None
        
        self.setHeaderLabel("SceneTree - Unknown")
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.context_menu)
        self.itemClicked.connect(self.clicked_item)

    def context_menu(self):
        menu = QMenu(self)
        create_empty = QAction("Create GameObject", self)
        create_empty.triggered.connect(lambda: self.create_gameobject("gameobject"))
        menu.addAction(create_empty)
        if len(self.selectedItems()) >= 1:
            menu.addSeparator()
            remove_entity = QAction("Remove GameObject", self)
            remove_entity.triggered.connect(self.remove_gameobject)
            menu.addAction(remove_entity)
        menu.exec_(QCursor.pos())

    def remove_gameobject(self):
        if len(self.selectedItems()) >= 1:
            obj = self.selectedItems()[0].obj
            if obj != self.scene:
                objs = [self.scene]
                parent = None
                while parent is None:
                    current = objs[0]
                    for child in current.childs:
                        if child == obj:
                            parent = current
                            break
                        else:
                            objs.append(child)
                parent.childs.remove(obj)
                self.parent.viewport.update_screen()
                self.parent.components.set_obj(parent)
                self.parent.project.save()
                self.update_items()
            else:
                QMessageBox.warning(self, "PyEngine4 - Remove GameObject", "Can't remove Scene")

    def create_gameobject(self, entity):
        if len(self.selectedItems()) > 1:
            obj = self.selectedItems()[0]
        else:
            obj = self.scene
        if entity == "gameobject":
            text = QInputDialog.getText(self, "PyEngine4 - Create GameObject", "GameObject Name:", QLineEdit.Normal)
            if text[1] and len(text[0]) > 0:
                new = GameObject(text[0])
                obj.childs.append(new)
                self.parent.viewport.update_screen()
                self.parent.components.set_obj(new)
                self.parent.project.save()
                self.update_items()
    
    def update_scene(self, scene):
        self.scene = scene
        self.setHeaderLabel("SceneTree - "+scene.name.capitalize())
        self.parent.viewport.update_screen()
        self.parent.components.set_obj(scene)
        self.update_items()
    
    def update_items(self):
        self.clear()

        treeitem = GameObjectItem([self.scene.name], self.scene)
        self.setup_childs(treeitem, self.scene)
        self.addTopLevelItem(treeitem)

        self.expandAll()
    
    def setup_childs(self, widget, obj):
        for o in obj.childs:
            child = GameObjectItem([o.name], o)
            widget.addChild(child)
            self.setup_childs(child, o)
    
    def clicked_item(self, item, column):
        self.parent.components.set_obj(item.obj)
