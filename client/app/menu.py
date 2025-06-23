from PyQt5.QtWidgets import QPushButton, QLabel, QWidget
from PyQt5.QtCore import QRect, QMetaObject

class Ui_MenuWindow(object):
    def setupUi(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.text_label = QLabel("UID: ", self.centralwidget)
        self.text_label.setGeometry(QRect(150, 50, 200, 30))

        self.search_button = QPushButton("Search Records", self.centralwidget)
        self.search_button.setGeometry(QRect(100, 100, 200, 30))
        self.search_button.clicked.connect(MainWindow.on_search_button_clicked)

        self.view_button = QPushButton("View Record", self.centralwidget)
        self.view_button.setGeometry(QRect(100, 140, 200, 30))
        self.view_button.clicked.connect(MainWindow.on_view_button_clicked)

        self.upload_button = QPushButton("Upload Record", self.centralwidget)
        self.upload_button.setGeometry(QRect(100, 180, 200, 30))
        self.upload_button.clicked.connect(MainWindow.on_upload_button_clicked)

        self.back_button = QPushButton("Logout", self.centralwidget)
        self.back_button.setGeometry(QRect(100, 220, 200, 30))
        self.back_button.clicked.connect(MainWindow.on_back_button_clicked)

        QMetaObject.connectSlotsByName(MainWindow)
