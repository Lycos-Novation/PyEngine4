import os

from pyengine.common.project import Project


class ProjectManager:
    def __init__(self):
        self.projects = []

    def create_project(self, name, author, icon):
        self.projects.append(Project(name, author, icon))
    
    def load_projects(self):
        for i in os.listdir("projects"):
            self.projects.append(Project.load(os.path.join("projects", i)))

    def exist(self, name):
        for i in self.projects:
            if i.name == name:
                return True
        return False
