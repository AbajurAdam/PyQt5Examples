import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Gui(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(500, 500, 350, 250)
        self.setWindowTitle('Gui With Message')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(
            self, 'Mesaj', "Do you really want to quit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())
