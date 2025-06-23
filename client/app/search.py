from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QComboBox, QWidget
from PyQt5.QtCore import QRect, QMetaObject

class Ui_SearchWindow(object):
    def setupUi(self, MainWindow):
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)

        self.userid_textbox = QLineEdit(self.centralwidget)
        self.userid_textbox.setGeometry(QRect(100, 50, 200, 30))
        self.userid_textbox.setPlaceholderText("Patient UID")

        self.name_textbox = QLineEdit(self.centralwidget)
        self.name_textbox.setGeometry(QRect(100, 90, 200, 30))
        self.name_textbox.setPlaceholderText("Patient Name")

        self.combo_box = QComboBox(self.centralwidget)
        self.combo_box.setGeometry(QRect(100, 130, 200, 30))
        self.combo_box.addItems(["health_record", "medicine_record", "financial_record", "research_record"])

        self.search_api_button = QPushButton("Search", self.centralwidget)
        self.search_api_button.setGeometry(QRect(100, 170, 200, 30))
        self.search_api_button.clicked.connect(MainWindow.on_search_api_button_clicked)

        self.back_button = QPushButton("Back", self.centralwidget)
        self.back_button.setGeometry(QRect(100, 210, 200, 30))
        self.back_button.clicked.connect(MainWindow.on_back_button_clicked)

        QMetaObject.connectSlotsByName(MainWindow)
