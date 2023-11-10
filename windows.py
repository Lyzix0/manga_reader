import sys
from main_menu import Ui_MainWindow
from PyQt6.QtGui import QWindow, QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


class Main_Menu_Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start()

    def start(self):
        self.setWindowTitle("Главное меню")

        self.image = QPixmap("images/1111.png").scaled(200, 150)
        self.icon = QIcon(self.image)
        self.pushButton_5.setIcon(self.icon)
        self.pushButton_5.setIconSize(self.image.rect().size())
        self.pushButton_5.clicked.connect(self.image_click)

    def image_click(self):
        print("a")


if __name__ == "__main__":
    application = QApplication(sys.argv)
    qt = Main_Menu_Window()
    qt.show()
    sys.exit(application.exec())
