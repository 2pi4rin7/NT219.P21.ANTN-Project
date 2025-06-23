from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QComboBox, QWidget
from PyQt5.QtCore import QRect, QMetaObject

class Ui_ViewWindow(object):
    def setupUi(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.UID = QLineEdit(self.centralwidget)
        self.UID.setGeometry(QRect(100, 50, 200, 30))
        self.UID.setPlaceholderText("Patient UID")

        self.collection = QComboBox(self.centralwidget)
        self.collection.setGeometry(QRect(100, 90, 200, 30))
        self.collection.addItems(["health_record", "medicine_record", "financial_record", "research_record"])

        self.view_api_button = QPushButton("View Record", self.centralwidget)
        self.view_api_button.setGeometry(QRect(100, 130, 200, 30))
        self.view_api_button.clicked.connect(MainWindow.on_view_api_button_clicked)

        self.back_button = QPushButton("Back", self.centralwidget)
        self.back_button.setGeometry(QRect(100, 170, 200, 30))
        self.back_button.clicked.connect(MainWindow.on_back_button_clicked)

        QMetaObject.connectSlotsByName(MainWindow)
