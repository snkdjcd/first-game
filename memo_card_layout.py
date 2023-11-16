from PyQt5.QtCore import*
from PyQt5.QtWidgets import*

btn_menu = QPushButton("Меню")
btn_sleep = QPushButton("Відпочити")
box_minutes = QSpinBox()
box_minutes.setVlue(30)
slp_text = QLabel("хвилин")
btn_answer = QPushButton("Відповісти")

text_question = QLabel("")
question_group_box = QGroupBox("Варіанти відповідей")
btn_group = QButtonGroup()

rbt1 = QRadioButton()
rbt2 = QRadioButton()
rbt3 = QRadioButton()
rbt4 = QRadioButton()

btn_group.addButton(rbt1)
btn_group.addButton(rbt2)
btn_group.addButton(rbt3)
btn_group.addButton(rbt4)

answer_group_box = QGroupBox("Результати тесту")
text_res = QLabel()
text_correct = QLabel()

layout_question = QHBoxLayout()
layout_question1 = QVBoxLayout()
layout_question2 = QVBoxLayout()

layout_question1.addWidget(rbt1)
layout_question1.addWidget(rbt2)
layout_question2.addWidget(rbt3)
layout_question2.addWidget(rbt4)
layout_question.addLayout(layout_question1)
layout_question.addLayout(layout_question2)
question_group_box.setLayout(layout_question)

layout_answer = QVBoxLayout()
layout_answer.addWidget(text_res, alignment=(Qt.AlignTop | Qt.AlignLeft))
layout_answer.addWidget(text_correct, alignment=Qt.AlignCenter)
answer_group_box.setLayout(layout_answer)
answer_group_box.hide()

line1 = QHBoxLayout()
line1.addWidget(btn_menu)
line1.addStretch(1)
line1.addWidget(btn_sleep)
line1.addWidget(box_minutes)
line1.addWidget(slp_text)

line2 = QHBoxLayout()
line2.addWidget(text_question)

line3 = QHBoxLayout()
line3.addWidget(question_group_box)
line3.addWidget(answer_group_box)

line4 = QHBoxLayout()
# line4.addSpacing(1)
line4.addWidget(btn_answer, stretch=2)
# line4.addSpacing(1)

main_line = QVBoxLayout()
main_line.addLayout(line1, stretch=1)
main_line.addLayout(line2, stretch=2)
main_line.addLayout(line3, stretch=8)
main_line.addSpacing(1)
main_line.addLayout(line4, stretch=1)
main_line.addSpacing(1)

def show_res():
    question_group_box.hide()
    answer_group_box.show()
    btn_answer.setText("Наступне питання")

def show_question():
    question_group_box.show()
    answer_group_box.hide()
    btn_answer.setText("Відповісти")
    btn_group.setExclusive(False)
    rbt1.setChecked(False)
    rbt2.setChecked(False)
    rbt3.setChecked(False)
    rbt4.setChecked(False)
    btn_group.setExclusive(True)
