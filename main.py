from PyQt5.QtWidgets import*

app = QApplication([])
okno = QWidget()

okno.setWindowTitle('Определения')
okno.resize(400,400)

but2 = QPushButton(okno)
but2.setText('Переменный ток')
#line1.addWidget(but2)
but2.move(10,10)

def popwin():
    okno2 = QMessageBox()
    okno2.setText('Переме́нный ток — электрический ток, который с течением времени изменяется по величине, обычно и по направлению в электрической цепи.')
    okno2.exec_()
but2.clicked.connect(popwin)

but3 = QPushButton(okno)
but3.setText('Молекула')
#line1.addWidget(but2)
but3.move(110,10)

def popwin2():
    okno3 = QMessageBox()
    okno3.setText('Мельчайшая частица данного вещества.')
    okno3.exec_()
but3.clicked.connect(popwin2)

but4 = QPushButton(okno)
but4.setText('Механическое движение')
#line1.addWidget(but2)
but4.move(200,10)

def popwin3():
    okno4 = QMessageBox()
    okno4.setText('Изменение положения тела относительно других тел с течением времени.')
    okno4.exec_()
but4.clicked.connect(popwin3)

but5 = QPushButton(okno)
but5.setText('Тормозной путь.')
#line1.addWidget(but2)
but5.move(10,50)

def popwin4():
    okno5 = QMessageBox()
    okno5.setText('Путь, который проходит автомобиль после выключения двигателя до полной остановки.')
    okno5.exec_()
but5.clicked.connect(popwin4)

but6 = QPushButton(okno)
but6.setText('Скорость')
#line1.addWidget(but2)
but6.move(110,50)

def popwin5():
    okno6 = QMessageBox()
    okno6.setText('Величина, равная отношению пути ко времени, за которое этот путь пройден.')
    okno6.exec_()
but6.clicked.connect(popwin5)

but7 = QPushButton(okno)
but7.setText('Равнодействующая сила')
#line1.addWidget(but2)
but7.move(200,50)

def popwin5():
    okno7 = QMessageBox()
    okno7.setText('Сила, которая производит на тело такое же  действие, как несколько одновременно действующих сил.')
    okno7.exec_()
but7.clicked.connect(popwin5)

but8 = QPushButton(okno)
but8.setText('Газовые турбины')
#line1.addWidget(but2)
but8.move(10,90)

def popwin5():
    okno8 = QMessageBox()
    okno8.setText('Двигатель, в котором компрессор сжимает атмосферный воздух, увеличивая его давление в 5-10 раз. Топливо (керосин, мазут) и горячий воздух попадает в камеры сгорания, в которой продукты горения имеют высокую температуру и, расширяясь, движутся с высокой скоростью. Применяются в авиации, т.к. обладают при сравнительно небольших размерах большой мощностью. КПД 25-30%')
    okno8.exec_()
but8.clicked.connect(popwin5)

but9 = QPushButton(okno)
but9.setText('Конвекция')
#line1.addWidget(but2)
but9.move(110,90)

def popwin5():
    okno9 = QMessageBox()
    okno9.setText('Теплообмен, происходящий благодаря переносу энергии перемещающимися слоями жидкости и газа.')
    okno9.exec_()
but9.clicked.connect(popwin5)

but10= QPushButton(okno)
but10.setText('Количество теплоты')
#line1.addWidget(but2)
but10.move(200,90)

def popwin5():
    okno10 = QMessageBox()
    okno10.setText('Энергия, которую тело получает или отдает в результате теплообмена.')
    okno10.exec_()
but10.clicked.connect(popwin5)

but11= QPushButton(okno)
but11.setText('Излучение')
#line1.addWidget(but2)
but11.move(10,130)

def popwin5():
    okno11 = QMessageBox()
    okno11.setText('Вид теплообмена, при котором внутренняя энергия передается струями и потоками.')
    okno11.exec_()
but11.clicked.connect(popwin5)

but12= QPushButton(okno)
but12.setText('Схема')
#line1.addWidget(but2)
but12.move(110,130)

def popwin5():
    okno12 = QMessageBox()
    okno12.setText('Упрощенное изображение чего-либо.')
    okno12.exec_()
but12.clicked.connect(popwin5)

but13= QPushButton(okno)
but13.setText('Тепловой двигатель')
#line1.addWidget(but2)
but13.move(200,130)

def popwin5():
    okno13 = QMessageBox()
    okno13.setText('Устройство, которыми совершается механическая работа за счет внутренней энергии топлива.')
    okno13.exec_()
but13.clicked.connect(popwin5)

but14= QPushButton(okno)
but14.setText('Плавление')
#line1.addWidget(but2)
but14.move(10,170)

def popwin5():
    okno14 = QMessageBox()
    okno14.setText('Явление перехода из кристаллического вещества в жидкое состояние.')
    okno14.exec_()
but14.clicked.connect(popwin5)

but15= QPushButton(okno)
but15.setText('Испарение')
#line1.addWidget(but2)
but15.move(110,170)

def popwin5():
    okno15 = QMessageBox()
    okno15.setText('Явление перехода вещества из жидкого состояния в газообразное.')
    okno15.exec_()
but15.clicked.connect(popwin5)

but16= QPushButton(okno)
but16.setText('Насыщенный пар')
#line1.addWidget(but2)
but16.move(200,170)

def popwin5():
    okno16 = QMessageBox()
    okno16.setText('Пар, находящийся в равновесии со своей жидкостью.')
    okno16.exec_()
but16.clicked.connect(popwin5)

but17= QPushButton(okno)
but17.setText('Психрометр')
#line1.addWidget(but2)
but17.move(10,210)

def popwin5():
    okno17 = QMessageBox()
    okno17.setText('Прибор для измерения относительной влажности воздуха.')
    okno17.exec_()
but17.clicked.connect(popwin5)

but18= QPushButton(okno)
but18.setText('Кипение')
#line1.addWidget(but2)
but18.move(110,210)

def popwin5():
    okno18 = QMessageBox()
    okno18.setText('Превращение жидкости в пар путем образования пузырьков пара по всему объему жидкости.')
    okno18.exec_()
but18.clicked.connect(popwin5)

but19= QPushButton(okno)
but19.setText('Температура кипения')
#line1.addWidget(but2)
but19.move(200,210)

def popwin5():
    okno19 = QMessageBox()
    okno19.setText('Температура, при которой жидкость кипит.')
    okno19.exec_()
but19.clicked.connect(popwin5)

but20= QPushButton(okno)
but20.setText('Электризация')
#line1.addWidget(but2)
but20.move(10,250)

def popwin5():
    okno20 = QMessageBox()
    okno20.setText('Явление разделение электрических зарядов тела.')
    okno20.exec_()
but20.clicked.connect(popwin5)

but21= QPushButton(okno)
but21.setText('Проводник')
#line1.addWidget(but2)
but21.move(110,250)

def popwin5():
    okno21 = QMessageBox()
    okno21.setText('Вещество, среда, материал, хорошо проводящие электрический ток.')
    okno21.exec_()
but21.clicked.connect(popwin5)

but22= QPushButton(okno)
but22.setText('Электрическое поле')
#line1.addWidget(but2)
but22.move(200,250)

def popwin5():
    okno22 = QMessageBox()
    okno22.setText('Особая форма материи вокруг электрических зарядов.')
    okno22.exec_()
but22.clicked.connect(popwin5)

but23= QPushButton(okno)
but23.setText('Конденсатор')
#line1.addWidget(but2)
but23.move(10,290)

def popwin5():
    okno23 = QMessageBox()
    okno23.setText('Прибор для накопления зарядов, энергии электрического поля.')
    okno23.exec_()
but23.clicked.connect(popwin5)

but24= QPushButton(okno)
but24.setText('Кулон')
#line1.addWidget(but2)
but24.move(110,290)

def popwin5():
    okno24 = QMessageBox()
    okno24.setText('Единица измерения заряда.')
    okno24.exec_()
but24.clicked.connect(popwin5)

but25= QPushButton(okno)
but25.setText('Короткое замыкание')
#line1.addWidget(but2)
but25.move(200,290)

def popwin5():
    okno25 = QMessageBox()
    okno25.setText('Замыкание в электрической цепи, приводящее к тому, что сопротивление цепи становится крайне мал, а сила тока - очень большой.')
    okno25.exec_()
but25.clicked.connect(popwin5)

okno.setStyleSheet('''QWidget{background-image: url('aaaa.jpg');
}''')

but2.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but3.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but4.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but5.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but6.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but7.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but8.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but9.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but10.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but11.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but12.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but13.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but14.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but15.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but16.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but17.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but18.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but19.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but20.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but21.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but22.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but23.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but24.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')
but25.setStyleSheet('''QPushButton{font-size:10px;
background: white;}''')

okno.show()
app.exec_()