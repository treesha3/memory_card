from PyQt5.QtCore import Qt
from random import shuffle
from random import randint
from PyQt5.QtWidgets import QApplication,QButtonGroup, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QMessageBox,QHBoxLayout, QGroupBox



class Question():
    def __init__(self, question, right_ans, wrong1, wrong2, wrong3):
        self.question = question
        self.right_ans = right_ans
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


question_list = []
question_list.append(
    Question(
        'Какой язык в россии?',
        "русский","китайский", "английский", "казахский"

    )
)

question_list.append(
    Question(
        'Что растет на яблоне',
        "Яблоки","Малина", "Клубника", "Груша"

    )
)

question_list.append(
    Question(
        'Формула дискриминанта',
        "b*b - 4ac","b*b + 4ac", "b + b - 4ac", "b - b * 10 - 4ac"

    )
)

question_list.append(
    Question(
        'Как найти площадь квадрата',
        "a*a","a * a / 2", "зачем ее искать", "a+a+a+a"

    )
)

question_list.append(
    Question(
        'Как создать ФУНКЦИЮ?',
        "def()","class()", "function()", "class(def())"

    )
)

question_list.append(
    Question(
        'что из этого язык программирования?',
        "Python","Mumuthon", "Sercte", "Demote"

    )
)


app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('что то ')
main_window.resize(300,200)
printet = QLabel('Какой национальности не существует')
btn_ok = QPushButton('Ответить')




RadioGroupBox = QGroupBox('Варианты ответов')
r1 = QRadioButton('Энцы')
r2 = QRadioButton('Бебенцы')
r3 = QRadioButton('Перелецы')
r4 = QRadioButton('Леленцы')

RadioGroup = QButtonGroup()
RadioGroup.addButton(r1)
RadioGroup.addButton(r2)
RadioGroup.addButton(r3)
RadioGroup.addButton(r4)




layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(r1)
layout_ans2.addWidget(r2)
layout_ans3.addWidget(r3)
layout_ans3.addWidget(r4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)


AnsGroupBox = QGroupBox('Здесь будет правильный ответ')
a1 = QLabel('Правильно/Не правильно')
a2 = QLabel('Правильный ответ')

l1 = QVBoxLayout()
l1.addWidget(a1, alignment = (Qt.AlignLeft | Qt.AlignTop))
l1.addWidget(a2,alignment = Qt.AlignCenter, stretch = 2)
AnsGroupBox.setLayout(l1)

layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    r1.setChecked(False)
    r2.setChecked(False)
    r3.setChecked(False)
    r4.setChecked(False)
    RadioGroup.setExclusive(True)


answers = [r1, r2, r3 ,r4]



def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    printet.setText(q.question)
    a2.setText(q.right_ans)
    show_question()

def show_correct(res):
    a1.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_window.score += 1
        
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')



def next_questoin():
    main_window.total += 1
    print('Статистика:')
    print('----Всего вопросов:', main_window.total)
    print('----Их них правильно:', main_window.score)
    print('----Рейтинг:', main_window.score / main_window.total * 100, '%')
    cur_question = randint(0, len(question_list) - 1)
    q = question_list[cur_question]
    ask(q)


def click_ok():
    if btn_ok == 'Ответить':
        check_answer()
    else:
        next_questoin()





btn_ok.clicked.connect(click_ok)


layout1.addWidget(printet, alignment = Qt.AlignCenter)
layout2.addWidget(RadioGroupBox)
layout2.addWidget(AnsGroupBox)

layout3.addStretch(1)
layout3.addWidget(btn_ok)
layout3.addStretch(1)
layout_main = QVBoxLayout()
layout_main.addLayout(layout1)
layout_main.addLayout(layout2)
layout_main.addLayout(layout3)


AnsGroupBox.hide()


main_window.setLayout(layout_main)
main_window.total = 0 
main_window.score = 0
next_questoin()
main_window.show()
app.exec_()
