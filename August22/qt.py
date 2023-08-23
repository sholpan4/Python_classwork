import os

from PyQt5.QtCore import QLibraryInfo
from PyQt5.QtWidgets import *

def set_qt_plugin_path():
    # qpa_path = QLibraryInfo.location(QLibraryInfo.PluginsPath)
    # qpa_path = qpa_path.encode('latin').decode('utf-8')
    os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = "venv/Lib/site-packages/PyQt5/Qt5/plugins/platforms"

app = QApplication([])
window = QMainWindow()

label = QLabel("Привет из Qt!")

window.setCentralWidget(label)
window.show()
app.exec()