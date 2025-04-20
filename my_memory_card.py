#создай приложение для запоминания информации
from random import shuffle
from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QRadioButton, QWidget, QVBoxLayout, QLabel, QPushButton, QButtonGroup, QHBoxLayout, QGroupBox 

class Question():
    def __init__(self, qst, right_answer, wrong1, wrong2, wrong3):
        self.qst = qst
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400,300)

main_layout = QVBoxLayout()
question = QLabel('Вопрос?')
btn_OK = QPushButton('Ответить')

ansBox = QGroupBox('Варианты Ответов:')
rbtn1 = QRadioButton('4')
rbtn2 = QRadioButton('3')
rbtn3 = QRadioButton('2')
rbtn4 = QRadioButton('1')
layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
ansBox.setLayout(layout_ans1)

resBox = QGroupBox('Результаты Теста:')
layout = QVBoxLayout()
result = QLabel('Правильно/Неправильно')
right_ans = QLabel('Правильный Ответ')
layout.addWidget(result)
layout.addWidget(right_ans, alignment= Qt.AlignCenter)
resBox.setLayout(layout)


layout_box = QHBoxLayout()
layout_box.addWidget(ansBox)
layout_box.addWidget(resBox)
resBox.hide()
main_layout.addWidget(question, alignment = Qt.AlignCenter)
main_layout.addLayout(layout_box)
main_layout.addWidget(btn_OK, alignment = Qt.AlignCenter)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

def show_result():
    ansBox.hide()
    resBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    ansBox.show()
    resBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

question_list = []
question_list.append(Question('Вопрос 2?', 'Ответ 1', 'Ответ 2', 'Ответ 3', 'Ответ 4'))
question_list.append(Question('Вопрос 3?', 'Ответ 3', 'Ответ 1', 'Ответ 4', 'Ответ 2'))
question_list.append(Question('Вопрос 4?', 'Ответ 2', 'Ответ 4', 'Ответ 3', 'Ответ 1'))

def next_question():
    main_win.total +=1
    cur_question = randint(0, len(question_list) -1)
    q = question_list[cur_question]
    ask(q)
    total = main_win.total
    score = main_win.score
    rating = (score / total) * 100
    print(f"Твоя статистика: {rating:.0f}%")

main_win.cur_question = -1

def start_test():
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()

answer = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong1)
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    right_ans.setText(q.right_answer)
    question.setText(q.qst)
    show_question()

q = Question('Вопрос 1?', 'Ответ 4', 'Ответ 2', 'Ответ 1', 'Ответ 2')
ask(q)

def check_answer():
    if answer[0].isChecked():
        show_correct('Верно')
        main_win.score += 1
    elif answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
        show_correct('Неверно')
    

def show_correct(res):
    result.setText(res)
    show_result()

btn_OK.clicked.connect(start_test)

main_win.score = 0
main_win.total = 0

main_win.setLayout(main_layout)
main_win.show()
app.exec_()