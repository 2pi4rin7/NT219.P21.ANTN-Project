from PyQt5.QtWidgets import (
    QWidget, QLineEdit, QPushButton, QMainWindow
)
from PyQt5.QtCore import QRect, QMetaObject

class Ui_LoginWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("LoginWindow")
        MainWindow.resize(400, 300)

        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        # Username Input
        self.username_textbox = QLineEdit(self.centralwidget)
        self.username_textbox.setGeometry(QRect(100, 80, 200, 30))
        self.username_textbox.setPlaceholderText("Username")
        self.username_textbox.setObjectName("username_textbox")

        # Password Input
        self.password_textbox = QLineEdit(self.centralwidget)
        self.password_textbox.setGeometry(QRect(100, 130, 200, 30))
        self.password_textbox.setEchoMode(QLineEdit.Password)
        self.password_textbox.setPlaceholderText("Password")
        self.password_textbox.setObjectName("password_textbox")

        # Login Button
        self.pushButton = QPushButton("Login", self.centralwidget)
        self.pushButton.setGeometry(QRect(100, 180, 200, 30))
        self.pushButton.setObjectName("login_button")
        self.pushButton.clicked.connect(MainWindow.on_pushButton_clicked)

        # Kết nối các slot được khai báo bằng @pyqtSlot trong MainWindow
        QMetaObject.connectSlotsByName(MainWindow)
