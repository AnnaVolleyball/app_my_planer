
# -*- coding: UTF-8 -*-

import sqlite3
import sys
import csv

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QButtonGroup, QTableWidgetItem, QFileDialog
from pyqtgraph import mkPen

from Project2 import Ui_Registration
from Project1 import Ui_WorkWindow


class WorkWindow(QMainWindow, Ui_WorkWindow):
    def __init__(self, userId=-1, connection=None):
        super().__init__()
        self.setupUi(self)
        self.userId = userId
        self.connection = connection
        self.cursor = self.connection.cursor()
        self.graphicsView.setBackground('white')
        self.tasks_count = 0
        self.tasks = []
        self.pushButton.clicked.connect(self.push_save_mood)
        self.button_group1 = QButtonGroup()
        self.button_group1.addButton(self.radioButton)
        self.button_group1.addButton(self.radioButton_2)
        self.button_group1.addButton(self.radioButton_3)
        self.button_group1.addButton(self.radioButton_4)
        self.button_group1.addButton(self.radioButton_5)
        self.pushButton_2.clicked.connect(self.push_make_graf)
        self.pushButton_3.clicked.connect(self.add_empty_task)
        self.pushButton_4.clicked.connect(self.save_task)
        self.pushButton_5.clicked.connect(self.books_from_file)
        self.pushButton_6.clicked.connect(self.books_to_file)
        self.pushButton_7.clicked.connect(self.update_matrix)
        self.pushButton_8.clicked.connect(self.delete_all_tasks)
        self.pushButton_9.clicked.connect(self.delete_book)
        self.pushButton_10.clicked.connect(self.add_book)
        self.add_task_from_db()
        self.print_books()

    def push_save_mood(self):
        if self.button_group1.checkedButton():
            title = self.button_group1.checkedButton().text()
            self.cursor.execute(f"""INSERT INTO Screen(mood_id) 
                                    VALUES ((SELECT id FROM Moods
                                    WHERE title = '{title}'))""")
            self.statusbar.showMessage("Настроение на сегодня сохранено!")
            self.connection.commit()
        else:
            self.statusbar.showMessage("Прежде чем сохранить настроение, его нужно выбрать!")

    def push_make_graf(self):
        result = self.cursor.execute(f"""SELECT mood_id FROM Screen
                                         ORDER BY id DESC LIMIT 7""").fetchall()
        if len(result) >= 2:
            res = [x[0] for x in result]
            res.reverse()
            self.graphicsView.clear()
            self.graphicsView.setBackground('white')
            pen = mkPen('pink', width=3)
            self.graphicsView.plot([i for i in range(1, len(res) + 1)], res, pen=pen)
        else:
            self.statusbar.showMessage("Пока что в твоем дневнике не хватает настроений, чтобы построить график :(")

    def add_task_from_db(self):
        result = self.cursor.execute(f"""SELECT * FROM Tasks ORDER BY id""").fetchall()
        for i in result:
            self.add_task(*i)

    def add_empty_task(self):
        self.add_task(self.tasks_count, '', True, True, False)
        self.cursor.execute(f"""INSERT INTO Tasks 
                                VALUES ({self.tasks_count - 1}, '', {True}, {True}, {False})""")
        self.connection.commit()

    def add_task(self, task_id, title, vazh, srok, done):
        if self.tasks_count == 8:
            self.statusbar.showMessage("На сегодня задач достаточно :(")
            return

        self.tasks.append({})
        self.tasks[task_id]['id'] = task_id
        temp = QtWidgets.QLineEdit(self.frame_3)
        temp.setText(title)
        temp.setGeometry(QtCore.QRect(10, 10 + task_id * 55, 391, 41))
        temp.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                           "border: 1px solid rgb(85, 85, 85);\n"
                           "border-radius: 10;")
        temp.setObjectName("task_lineEdit" + str(task_id))
        self.tasks[task_id]['title'] = temp
        self.tasks[task_id]['title'].show()

        temp1 = QtWidgets.QRadioButton(self.frame_3)
        temp1.setGeometry(QtCore.QRect(420, 20 + task_id * 55, 95, 20))
        temp1.setText("")
        temp1.setObjectName("fast_radioButton" + str(task_id))
        self.tasks[task_id]['fast'] = temp1
        self.tasks[task_id]['fast'].show()

        temp2 = QtWidgets.QRadioButton(self.frame_3)
        temp2.setGeometry(QtCore.QRect(500, 20 + task_id * 55, 95, 20))
        temp2.setText("")
        temp2.setObjectName("unfast_radioButton" + str(task_id))
        self.tasks[task_id]['unfast'] = temp2
        self.tasks[task_id]['unfast'].show()

        temp3 = QtWidgets.QRadioButton(self.frame_3)
        temp3.setGeometry(QtCore.QRect(580, 20 + task_id * 55, 95, 20))
        temp3.setText("")
        temp3.setObjectName("imp_radioButton" + str(task_id))
        self.tasks[task_id]['imp'] = temp3
        self.tasks[task_id]['imp'].show()

        temp4 = QtWidgets.QRadioButton(self.frame_3)
        temp4.setGeometry(QtCore.QRect(660, 20 + task_id * 55, 95, 20))
        temp4.setText("")
        temp4.setObjectName("unimp_radioButton" + str(task_id))
        self.tasks[task_id]['unimp'] = temp4
        self.tasks[task_id]['unimp'].show()

        self.tasks[task_id]['group_vazh'] = QButtonGroup()
        self.tasks[task_id]['group_vazh'].addButton(self.tasks[task_id]['imp'])
        self.tasks[task_id]['group_vazh'].addButton(self.tasks[task_id]['unimp'])
        self.tasks[task_id]['group_srok'] = QButtonGroup()
        self.tasks[task_id]['group_srok'].addButton(self.tasks[task_id]['fast'])
        self.tasks[task_id]['group_srok'].addButton(self.tasks[task_id]['unfast'])

        self.tasks[task_id]['checkBox'] = QtWidgets.QCheckBox(self.frame_3)
        self.tasks[task_id]['checkBox'].setGeometry(QtCore.QRect(750, 20 + task_id * 55, 111, 20))
        self.tasks[task_id]['checkBox'].setText("")
        self.tasks[task_id]['checkBox'].setObjectName("checkBox" + str(task_id))
        self.tasks[task_id]['checkBox'].show()

        self.tasks[task_id]['fast'].setChecked(srok)
        self.tasks[task_id]['imp'].setChecked(vazh)
        self.tasks[task_id]['checkBox'].setChecked(done)

        if self.tasks_count <= task_id:
            self.tasks_count += 1

    def save_task(self):
        for i in self.tasks:
            id = i['id']
            title = i['title'].text()
            vazh = i['imp'].isChecked()
            srok = i['fast'].isChecked()
            done = i['checkBox'].isChecked()
            self.cursor.execute(f"""UPDATE Tasks SET
                                    title = '{title}', vazh = {vazh}, srok = {srok}, done = {done}
                                    WHERE id = {id}""")
        self.connection.commit()
        self.statusbar.showMessage("Задачи успешно сохранены!")

    def update_matrix(self):
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.listWidget_3.clear()
        self.listWidget_4.clear()
        self.listWidget_5.clear()
        result = self.cursor.execute(f"""SELECT * FROM Tasks ORDER BY id""").fetchall()
        stroka = ''
        stroka2 = ''
        stroka3 = ''
        stroka4 = ''
        stroka5 = ''
        for i in result:
            title = i[1]
            vazh = i[2]
            srok = i[3]
            done = i[4]
            if done:
                stroka5 += '   • ' + title + '\n'
            elif vazh and srok:
                stroka += '   • ' + title + '\n'
            elif vazh and not srok:
                stroka2 += '   • ' + title + '\n'
            elif not vazh and srok:
                stroka3 += '   • ' + title + '\n'
            else:
                stroka4 += '   • ' + title + '\n'
        self.listWidget.addItem(stroka)
        self.listWidget_2.addItem(stroka2)
        self.listWidget_3.addItem(stroka3)
        self.listWidget_4.addItem(stroka4)
        self.listWidget_5.addItem(stroka5)
        self.statusbar.showMessage("Матрица успешно обновлена!")

    def delete_all_tasks(self):
        self.cursor.execute(f"""DELETE FROM Tasks""")
        self.connection.commit()
        self.tasks_count = 0
        for i in self.tasks:
            i["checkBox"].deleteLater()
            i["fast"].deleteLater()
            i["imp"].deleteLater()
            i["unimp"].deleteLater()
            i["unfast"].deleteLater()
            i["title"].deleteLater()
        self.tasks.clear()
        self.show()
        self.statusbar.showMessage("Все задачи удалены!")

    def add_book(self):
        title = self.lineEdit_3.text()
        if not title:
            self.statusbar.showMessage("Нужно ввести хотя бы название книги!")
            return
        author = self.lineEdit_2.text()
        zhanr = self.lineEdit_4.text()
        self.cursor.execute(f"""INSERT INTO Books (title, author, zhanr) VALUES('{title}', '{author}', '{zhanr}')""")
        id = self.cursor.lastrowid
        self.connection.commit()
        self.print_books()

    def print_books(self):
        result = self.cursor.execute(f"""SELECT * FROM Books""").fetchall()
        if not result:
            return
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = ['id', 'Название', 'Автор', 'Жанр']
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.tableWidget.setHorizontalHeaderLabels(["id", "Название", "Автор", "Жанр"])

    def delete_book(self):
        id = self.lineEdit_5.text()
        self.cursor.execute(f"""DELETE FROM Books WHERE id = '{id}'""")
        if not self.cursor.rowcount:
            self.statusbar.showMessage("Книги с таким номером нет :(")
        self.connection.commit()
        self.print_books()

    def books_from_file(self):
        file = QFileDialog.getOpenFileName(
            self, 'Выбрать csv-файл', '',
            'csv-файл (*.csv);;Все файлы (*)')[0]
        with open(file, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            for index, row in enumerate(reader):
                title = row[0]
                author = row[1]
                zhanr = row[2]
                self.cursor.execute(
                    f"""INSERT INTO Books (title, author, zhanr) VALUES('{title}', '{author}', '{zhanr}')""")
                self.connection.commit()
        self.print_books()

    def books_to_file(self):
        with open('results.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"',
                quoting=csv.QUOTE_MINIMAL)
            for i in range(self.tableWidget.rowCount()):
                row = []
                for j in range(1, self.tableWidget.columnCount()):
                    item = self.tableWidget.item(i, j)
                    if item is not None:
                        row.append(item.text())
                writer.writerow(row)
        self.statusbar.showMessage("Книги сохранены в файл results.csv")


class RegistrationWindow(QMainWindow, Ui_Registration):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("MyPlaner.db")
        self.cur = self.connection.cursor()
        self.btn_in = self.pushButton
        self.btn_reg = self.pushButton_2
        self.btn_in.clicked.connect(self.push)
        self.btn_reg.clicked.connect(self.push_reg)

    def push(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        try:
            result = self.cur.execute(f"""SELECT login FROM Users 
                                          WHERE login = '{login}'
                                          AND password = '{password}'""").fetchone()
            if not result:
                self.label.setText("Неправильный логин или пароль!")
                return
            else:
                self.userId = self.cur.execute(f"""SELECT id FROM Users 
                                                   WHERE login = '{login}'
                                                   AND password = '{password}'""").fetchone()[0]
            self.secondWin = WorkWindow(self.userId, self.connection)
            self.secondWin.show()
            self.close()
        except Exception as e:
            print(e)

    def push_reg(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        try:
            result = self.cur.execute(f"""SELECT login 
                                          FROM Users""").fetchall()
            if result:
                self.label.setText("Зарегистрироваться можно только один раз!")
                return
            self.cur.execute(f"""INSERT INTO Users(login, password) 
                                 VALUES('{login}', '{password}')""")
            self.connection.commit()
            self.label.setText("Отлично! Теперь вы можете войти!")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationWindow()
    ex.show()
    sys.exit(app.exec())
