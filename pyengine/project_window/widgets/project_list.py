from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QAbstractItemView

from pyengine.project_window.widgets.project_abstract import ProjectAbstract


class ProjectList(QListWidget):
    def __init__(self, parent, projects):
        super().__init__(parent)
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.update_list(projects)
    
    def update_list(self, projects):
        self.clear()
        for i in projects:
            w = ProjectAbstract(self, i)
            wi = QListWidgetItem()
            wi.setSizeHint(w.sizeHint())
            self.addItem(wi)
            self.setItemWidget(wi, w)
