from PyQt5.QtWidgets import QTreeWidgetItem


class EntityItem(QTreeWidgetItem):
    def __init__(self, strs, obj):
        super().__init__(strs)
        self.obj = obj
