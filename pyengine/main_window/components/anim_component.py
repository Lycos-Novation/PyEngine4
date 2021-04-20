from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QGridLayout, QSpinBox, QListWidget, QListWidgetItem, \
    QPushButton, QInputDialog, QMessageBox, QAbstractItemView, QFileDialog, QLayout, QSizePolicy
from PyQt5.QtCore import Qt

import os

from pyengine.common.components import anim_component


class AnimSprite(QWidget):
    def __init__(self, parent, component, index):
        super().__init__(parent.anims_list)
        self.parent = parent
        self.component = component
        self.anim = self.component.anims[index]
        self.index = index

        self.name = QLabel(self.anim.name + " (" + self.anim.type_+")")
        self.select_files = QPushButton("Select Sprites", self)

        self.select_files.clicked.connect(self.change_value)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0, 1, 3)
        self.layout.addWidget(self.select_files, 0, 3, 1, 2)
        self.setLayout(self.layout)

    def change_value(self):
        files = QFileDialog.getOpenFileNames(
            self,
            "Open Sprites",
            self.parent.parent.parent.project.folders["textures"],
            "Sprites (*.json)"
        )
        if len(files[0]) > 0:
            self.component.anims[self.index].sprites = [os.path.basename(i.replace(".json", "")) for i in files[0]]
            self.parent.parent.parent.project.save()
            self.parent.parent.parent.viewport.update_screen()


class AnimSpriteSheet(QWidget):
    def __init__(self, parent, component, index):
        super().__init__(parent.anims_list)
        self.parent = parent
        self.component = component
        self.anim = self.component.anims[index]
        self.index = index

        self.name = QLabel(self.anim.name + " (" + self.anim.type_+")")
        self.select_file = QPushButton("Select SpriteSheet", self)
        self.sprite_number = QLabel("Sprite Number")
        self.sprite_number_spins = [QSpinBox(self), QSpinBox(self)]

        for k, v in enumerate(self.sprite_number_spins):
            v.setMinimum(1)
            v.setValue(self.anim.sprite_number[k])
            v.valueChanged.connect(self.change_value)
        self.select_file.clicked.connect(self.change_file)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 0, 1, 3)
        self.layout.addWidget(self.select_file, 0, 3, 1, 2)
        self.layout.addWidget(self.sprite_number, 1, 0)
        for k, v in enumerate(self.sprite_number_spins):
            self.layout.addWidget(v, 1, 1+2*k, 1, 2)
        self.setLayout(self.layout)

    def change_file(self):
        file_name = QFileDialog.getOpenFileName(
            self,
            "Open SpriteSheet",
            self.parent.parent.parent.project.folders["textures"],
            "SpriteSheet (*.json)"
        )
        if len(file_name[0]) > 0:
            self.change_value(file=file_name[0])

    def change_value(self, _=None, file=None):
        if file is not None:
            self.component.anims[self.index].sprite_sheet = os.path.basename(file.replace(".json", ""))
        self.component.anims[self.index].sprite_number = [i.value() for i in self.sprite_number_spins]
        self.parent.parent.parent.project.save()
        self.parent.parent.parent.viewport.update_screen()


class AnimComponent(QWidget):
    def __init__(self, parent, component):
        super().__init__(parent)
        self.parent = parent
        self.component = component
        self.is_shrink = False

        self.name = QLabel("Anim", self)
        self.name.setAlignment(Qt.AlignHCenter)
        self.delete_btn = QPushButton("Delete", self)
        self.fps = QLabel("FPS", self)
        self.fps_spin = QSpinBox(self)
        self.playing = QLabel("Playing", self)
        self.playing_edit = QLineEdit(self.component.playing, self)
        self.anims_list = QListWidget(self)
        self.anims_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.anims_add = QPushButton("Add Animation", self)
        self.anims_remove = QPushButton("Remove Animation", self)
        self.animations = QLabel("Animations", self)
        self.animations.setAlignment(Qt.AlignHCenter)

        for k, i in enumerate(self.component.anims):
            self.create_anim(i.name, i.type_, k)

        self.delete_btn.clicked.connect(self.delete)
        self.anims_add.clicked.connect(self.add_anim)
        self.anims_remove.clicked.connect(self.remove_anim)
        self.fps_spin.setValue(self.component.fps)
        self.fps_spin.valueChanged.connect(self.change_value)
        self.playing_edit.textChanged.connect(self.change_value)

        self.layout = QGridLayout()
        self.layout.addWidget(self.name, 0, 1, 1, 3)
        self.layout.addWidget(self.delete_btn, 0, 4)
        self.layout.addWidget(self.fps, 1, 0)
        self.layout.addWidget(self.fps_spin, 1, 1, 1, 4)
        self.layout.addWidget(self.playing, 2, 0)
        self.layout.addWidget(self.playing_edit, 2, 1, 1, 4)
        self.layout.addWidget(self.animations, 3, 0, 1, 5)
        self.layout.addWidget(self.anims_list, 4, 0, 1, 5)
        self.layout.addWidget(self.anims_add, 5, 0, 1, 2)
        self.layout.addWidget(self.anims_remove, 5, 3, 1, 2)
        self.setLayout(self.layout)

    def delete(self):
        self.parent.remove_component(self.component.name)

    def add_anim(self):
        text = QInputDialog.getText(self, "PyEngine4 - Create Anim", "Anim Name:", QLineEdit.Normal)
        if text[1] and len(text[0]) > 0:
            text2 = QInputDialog.getText(self, "PyEngine4 - Create Anim", "Anim Type (Sprite/Sheet):", QLineEdit.Normal)
            if text2[1] and len(text2[0]) > 0 and text2[0] in ("Sprite", "Sheet"):
                self.create_anim(text[0], text2[0])
            elif text2[1]:
                QMessageBox.warning(self, "PyEngine4 - Error", "Unknown Anim Type.\nType Known : Sprite, Sheet.")

    def remove_anim(self):
        if len(self.anims_list.selectedItems()) >= 1:
            widget = self.anims_list.itemWidget(self.anims_list.selectedItems()[0])
            for i in self.component.anims:
                if i.name == widget.anim.name:
                    self.component.anims.remove(i)
                    break
            self.parent.parent.project.save()
            self.parent.parent.assets_explorer.open_folder(self.parent.parent.assets_explorer.current_folder)
            self.parent.parent.viewport.update_screen()
            self.anims_list.takeItem(self.anims_list.row(self.anims_list.selectedItems()[0]))

    def create_anim(self, name, type_, k=None):
        if k is None:
            if name in [i.name for i in self.component.anims]:
                QMessageBox.warning(self, "PyEngine4 - Error", "This name is already taken.")
                return
            k = len(self.component.anims)
            if type_ == "Sprite":
                self.component.anims.append(anim_component.AnimSprite(name, []))
            elif type_ == "Sheet":
                self.component.anims.append(anim_component.AnimSpriteSheet(name, None))
            else:
                return

            self.parent.parent.project.save()
            self.parent.parent.assets_explorer.open_folder(self.parent.parent.assets_explorer.current_folder)
            self.parent.parent.viewport.update_screen()

        if type_ == "Sprite":
            w = AnimSprite(self, self.component, k)
        elif type_ == "Sheet":
            w = AnimSpriteSheet(self, self.component, k)
        else:
            return
        wi = QListWidgetItem()
        wi.setSizeHint(w.sizeHint())
        self.anims_list.addItem(wi)
        self.anims_list.setItemWidget(wi, w)

    def change_value(self):
        self.component.fps = self.fps_spin.value()
        self.component.playing = self.playing_edit.text()
        self.parent.parent.project.save()
        self.parent.parent.assets_explorer.open_folder(self.parent.parent.assets_explorer.current_folder)
        self.parent.parent.viewport.update_screen()
