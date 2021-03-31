from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

from pyengine import common
import pygame


class About(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.project = None
        self.setWindowTitle("PyEngine4 - About")
        self.resize(350, 350)
        title = QLabel("About PyEngine 4", self)
        pe4version = QLabel("PyEngine4 Version : "+common.__version__+" ("+common.__num_version__+")", self)
        pgversion = QLabel("PyGame Version : "+pygame.version.ver)
        sdlversion = QLabel("SDL Version : "+".".join(map(str, pygame.version.SDL)))
        thanks = QLabel("Thanks to LycosNovation.")
        creator = QLabel("Created by LavaPower.")

        title.setFont(QFont("arial", 20, 1))
        title.setAlignment(Qt.AlignHCenter)
        pe4version.setFont(QFont("arial", 14, 1))
        pe4version.setAlignment(Qt.AlignHCenter)
        pgversion.setFont(QFont("arial", 14, 1))
        pgversion.setAlignment(Qt.AlignHCenter)
        sdlversion.setFont(QFont("arial", 14, 1))
        sdlversion.setAlignment(Qt.AlignHCenter)
        thanks.setFont(QFont("arial", 14, 1))
        thanks.setAlignment(Qt.AlignHCenter)
        creator.setFont(QFont("arial", 14, 1))
        creator.setAlignment(Qt.AlignHCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(title)
        self.layout.addSpacing(15)
        self.layout.addWidget(pe4version)
        self.layout.addWidget(pgversion)
        self.layout.addWidget(sdlversion)
        self.layout.addSpacing(15)
        self.layout.addWidget(thanks)
        self.layout.addWidget(creator)
        self.layout.setContentsMargins(20, 10, 20, 10)
        self.setLayout(self.layout)
