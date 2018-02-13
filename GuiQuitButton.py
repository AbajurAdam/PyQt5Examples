import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class Gui(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        print("Gui Initalized.")
        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit Button')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Gui()
    sys.exit(app.exec_())
