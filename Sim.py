import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Start(QWidget):

    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Logic Gate Sim. => Erkan Ercan')
        self.setWindowIcon(QIcon('web.png'))
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    startWin = Start()
    sys.exit(app.exec_())
