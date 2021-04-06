import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from pyengine.project_window import ProjectWindow


def launch():
    os.putenv("QT_AUTO_SCREEN_SCALE_FACTOR", "1")

    app = QApplication(sys.argv)
    icon = QIcon(os.path.join("pyengine", "resources", 'logo.png'))
    app.setWindowIcon(icon)

    win = ProjectWindow()
    win.show()

    app.exec_()


if __name__ == '__main__':
    launch()
