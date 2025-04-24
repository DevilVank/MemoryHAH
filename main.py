#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel,QButtonGroup)
from random import shuffle, randint
from PyQt5.QtGui import *

class Question():
    def __init__(self,question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Рейтинг: ', (window.score/window.total*100), '%')
    else:
        show_correct('Неверно!')
        print('Рейтинг: ', (window.score/window.total*100), '%')

def next_question():
    window.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    ask(q)

app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(600,450)



def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

questions_list = []
questions_list.append(Question('Когда создали майнкрафт', '2011', '2012', '1678', '1679'))
questions_list.append(Question('Когда вышел айфон 14', '2022', '2010', '1908', '1264'))
questions_list.append(Question('Когда вышла Гта Сан Андреас', '2004', '2009', '2001', '2022'))
questions_list.append(Question('Когда вышла игра FlatOut 2', '2006', '2009', '2001', '2022'))
questions_list.append(Question('Когда вышла игра It takes two', '2021', '2009', '2001', '2022'))
questions_list.append(Question('Когда вышел фильм Веном последний танец', '2024', '2010', '2001', '2022'))
questions_list.append(Question('В каком году умер Александр 1', '1825', '2001', '2023', '1999'))
questions_list.append(Question('Когда Наполеон захватил Москву', '1812', '1799', '1766', '2022'))
questions_list.append(Question('Когда Пушкин написал своё первое 19 октября', '1825', '1999', '2015', '2022'))
questions_list.append(Question('Когда родился Лермонтов', '1814', '2005', '1067', '2012'))

lb_Question = QLabel('Какой самый дорогой айфон?') # текст вопроса
lb_Question.setStyleSheet('background-color: aqua')
lb_Question.setFont(QFont('Times', 20, QFont.Bold))

btn_OK = QPushButton('Ответить') # кнопка ответа
btn_OK.setStyleSheet('background-color: Green')
btn_OK.setFont(QFont('Times', 25))
RadioGroupBox = QGroupBox("Варианты ответов") 

rbtn_1 = QRadioButton('11')
rbtn_2 = QRadioButton('12')
rbtn_3 = QRadioButton('14')
rbtn_4 = QRadioButton('15')

rbtn_1.setStyleSheet('font: 14pt Arial')
rbtn_2.setStyleSheet('font: 14pt Arial')
rbtn_3.setStyleSheet('font: 14pt Arial')
rbtn_4.setStyleSheet('font: 14pt Arial')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) 
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результаты теста')
lb_Result = QLabel('прав ты или нет')
lb_Correct = QLabel('ответ будет тут')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]


window.setLayout(layout_card)

btn_OK.clicked.connect(click_OK)
window.score = 0
window.total = 0
next_question()

window.show()
app.exec_()