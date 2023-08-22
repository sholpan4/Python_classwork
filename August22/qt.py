from PyQt5.QtWidgets import *

app = QApplication([])
window = QMainWindow()

label = QLabel("Привет из Qt!")

window.setCentralWidget(label)
window.show()
app.exec()