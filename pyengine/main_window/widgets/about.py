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
        self.resize(400, 400)
        title = QLabel("About PyEngine 4", self)
        pe4version = QLabel("PyEngine4 Version : "+common.__version__+" ("+common.__num_version__+")", self)
        pgversion = QLabel("PyGame Version : "+pygame.version.ver)
        sdlversion = QLabel("SDL Version : "+".".join(map(str, pygame.version.SDL)))
        thanks = QLabel("Thanks to LycosNovation.")
        creator = QLabel("Created by LavaPower.")

        title.setFont(QFont("arial", 24, 1))
        title.setAlignment(Qt.AlignHCenter)
        pe4version.setFont(QFont("arial", 18, 1))
        pe4version.setAlignment(Qt.AlignHCenter)
        pgversion.setFont(QFont("arial", 18, 1))
        pgversion.setAlignment(Qt.AlignHCenter)
        sdlversion.setFont(QFont("arial", 18, 1))
        sdlversion.setAlignment(Qt.AlignHCenter)
        thanks.setFont(QFont("arial", 18, 1))
        thanks.setAlignment(Qt.AlignHCenter)
        creator.setFont(QFont("arial", 18, 1))
        creator.setAlignment(Qt.AlignHCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(title)
        self.layout.addSpacing(40)
        self.layout.addWidget(pe4version)
        self.layout.addSpacing(20)
        self.layout.addWidget(pgversion)
        self.layout.addSpacing(20)
        self.layout.addWidget(sdlversion)
        self.layout.addSpacing(20)
        self.layout.addWidget(thanks)
        self.layout.addSpacing(40)
        self.layout.addWidget(creator)
        self.layout.setContentsMargins(50, 10, 50, 10)
        self.setLayout(self.layout)
