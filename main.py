from PyQt5.QtWidgets import*

app = QApplication([])
okno = QWidget()

okno.setWindowTitle('Калькулятор')
okno.resize(500,500)

t1 = QLabel(okno)
t1.setText('Тут что-то написано?')
t1.move(300,360)

b1 = QPushButton(okno)
b1.setText('Нет')
b1.move(100,250)

from random import*

def react1():
    x = randint(0,250)
    y = randint(0,250)
    b1.move(x,y)
    w = randint(30,100)
    h = randint(30,100)
    b1.resize(w,h)
    t1.setText('ДА')
b1.clicked.connect(react1)



okno.show()
app.exec_()