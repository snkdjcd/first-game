from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import randint
def click():
    num = randint(1, 100)
    number.setText(str(num))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Перший додаток")
main_win.resize(400, 200)
main_win.move(600, 400)

text = QLabel("Натисни, щоб дізнатися переможця!")
number = QLabel("?")
button = QPushButton("Згенерувати!")

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(number, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
main_win.setLayout(line)

button.clicked.connect(click)
main_win.show()
app.exec()
