from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QTextBrowser, QPushButton, QMessageBox, QSpinBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
from random import choice
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Password generator")
        self.setStyleSheet("background-color:#21CFC7;color:black")
        self.setFixedSize(600, 600)
        
        lbl_heading = QLabel("Password Generator", self)
        lbl_heading.setFont(QFont("arial", 15))
        lbl_heading.setGeometry(200, 30, 200, 50)
        lbl_heading.setStyleSheet("background-color:#000;border:3px solid #C40606 ;color:#C40606")

        # length password
        lbl_len_password = QLabel("Enter password length : ", self)
        lbl_len_password.setFont(QFont("arial", 15))
        lbl_len_password.setGeometry(100, 100, 210, 50)

        self.length = QSpinBox(self)
        self.length.setFont(QFont("arial", 15))
        self.length.setStyleSheet("background-color:#fff;")
        self.length.setValue(8)
        self.length.setCursor(Qt.CursorShape.PointingHandCursor)
        self.length.setGeometry(330, 115, 180, 25)

        # create checkboxes
        self.upper_case = QCheckBox("Upper case", self)
        self.upper_case.setFont(QFont("arial", 15))
        self.upper_case.setCursor(Qt.CursorShape.PointingHandCursor)
        self.upper_case.setGeometry(35, 180, 125, 40)

        self.lower_case = QCheckBox("Lower case", self)
        self.lower_case.setFont(QFont("arial", 15))
        self.lower_case.setCursor(Qt.CursorShape.PointingHandCursor)
        self.lower_case.setGeometry(165, 180, 125, 40)

        self.number = QCheckBox("Number", self)
        self.number.setFont(QFont("arial", 15))
        self.number.setCursor(Qt.CursorShape.PointingHandCursor)
        self.number.setGeometry(295, 180, 100, 40)

        self.symbol = QCheckBox("Symbol", self)
        self.symbol.setFont(QFont("arial", 15))
        self.symbol.setCursor(Qt.CursorShape.PointingHandCursor)
        self.symbol.setGeometry(400, 180, 100, 40)

        self.space = QCheckBox("Space", self)
        self.space.setFont(QFont("arial", 15))
        self.space.setCursor(Qt.CursorShape.PointingHandCursor)
        self.space.setGeometry(500, 180, 100, 40)

        # create buttons
        self.btn_create = QPushButton("CREATE", self)
        self.btn_create.setFont(QFont("arial", 15))
        self.btn_create.setStyleSheet("background-color:#FF0000;")
        self.btn_create.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_create.setGeometry(120, 280, 150, 40)
        self.btn_create.clicked.connect(self.create_password)

        self.btn_history = QPushButton("HISTORY", self)
        self.btn_history.setFont(QFont("arial", 15))
        self.btn_history.setStyleSheet("background-color:#0036FF;")
        self.btn_history.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_history.setGeometry(320, 280, 150, 40)
        self.btn_history.clicked.connect(self.show_history)

        # create result label
        self.lbl_result = QLabel("Password :", self)
        self.lbl_result.setFont(QFont("arial", 15))
        self.lbl_result.setGeometry(50, 430, 100, 50)

        self.txt_result = QTextBrowser(self)
        self.txt_result.setStyleSheet("background-color:#fff;")
        self.txt_result.setFont(QFont("arial", 15))
        self.txt_result.setGeometry(180, 380, 350, 150)


    def set_password_setting(self):
        setting_list = list()
        if self.upper_case.isChecked():
            setting_list.append("upper case")
        if self.lower_case.isChecked():
            setting_list.append("lower case")
        if self.number.isChecked():
            setting_list.append("number")
        if self.symbol.isChecked():
            setting_list.append("symbol")
        if self.space.isChecked():
            setting_list.append("space")
        return setting_list


    def create_password(self):
        self.lbl_result.setText("Password :")
        setting_list = self.set_password_setting()
        length = self.length.value()
        try:
            assert len(setting_list) != 0, "You must select at least one of the above"
            assert length >= 6, "The length of the password must be at least 6 digits"
        except AssertionError as err:
            self.show_error(str(err))
        else:
            password = str()
            for _ in range(length):
                order = choice(setting_list)
                if order == "upper case":
                    char = choice(ascii_uppercase)
                elif order == "lower case":
                    char = choice(ascii_lowercase)
                elif order == "number":
                    char = choice(digits)
                elif order == "symbol":
                    char = choice(punctuation)
                else:
                    char = " "
                password += char
            self.txt_result.setText(password)
            self.add_history(password)


    def writhe_history(self, message):
        with open("history.txt", "a") as w:
            w.write(f"{message}\n{'- ' * 25}\n")
    

    def show_history(self):
        self.lbl_result.setText("History :")
        try:
            with open("history.txt", "r") as r:
                text = r.read()
                self.txt_result.setText(text)
        except FileNotFoundError:
            self.show_error("There is no history")


    def show_error(self, message):
        error = QMessageBox(QMessageBox.Icon.Critical, "Error", message, parent=self)
        error.setStyleSheet("background-color:#fff;")
        error.show()
    

    def add_history(self, message):
        text = f"Do you save this password?\n\n{message}"
        message_box = QMessageBox(QMessageBox.Icon.Question, "Save password", text, parent=self)
        message_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        message_box.setStyleSheet("background-color:white;")
        message_box.show()
        if message_box.exec() == QMessageBox.StandardButton.Yes:
            self.writhe_history(message)


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    root = Window()
    root.show()

    sys.exit(app.exec())