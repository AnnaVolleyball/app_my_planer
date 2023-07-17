# Qt-приложение "MyPlaner"
Данное приложение создано в качестве мини-дневника, где можно вести свои текущие дела.
Перед запуском приложения необходимо выполнить все нужные действия из пункта 1.
### 1. Установка и запуск приложения
Запустить приложение можно двумя способами:
* Запустить MyPlaner.exe, находящийся в папке dist
    

* Запустить скрипт: для этого необходима версия Python 3.9. Перед первым запуском необходимо выполнить команду 

    `pip install -r \путь\к\папке\requirements.txt`. 

    Запуск происходит командой 

    `python3 \путь\к\папке\main.py`.

Внимание: исполняемый файл и скрипт используют разные базы данных!
### 2. Вход и регистрация
При первом запуске приложения вам нужно придумать свой логин и пароль. При последующем входе нужно указывать именно их. 
Приложение не является многопользовательским, окно входа создано лишь для конденфицеальности ваших данных.
Логин и пароль восстановлению не подлежат.
### 3. Возможности приложения
После входа для вас будут доступны 4 окна:
* Экран настроения
* Задачи
* Матрица Эйзенхаузера
* Список литературы
##### 3.1 Экран настроения
Выбирать свое настроение можно сколько угодно раз, однако полезно следовать советам, написанным в приложении, 
так статистика будет более реальная.
После сохранения статистики в StatusBar выведется связанное с этим сообщение.
Вывести статистику можно тогда, когда в ней есть минимум 2 значения. В статистике выводятся последние 7 значений.
##### 3.2 Задачи
Максимально за 1 раз можно добавить только 9 задач. Статусы и текст задач
можно менять в любое время.
После записи и исправления всех нужных задач необходимо нажать кнопку "Сохранить". В StatusBar выведется
соответствующее сообщение.
При нажатии кнопки "Удалить задачи" удаляются абсолютно все задачи.
##### 3.3 Матрица Эйзенхаузера
После того, как задачи будут сохранены, с помощью кнопки "Обновить матрицу" можно на матрицу вывести задачи. Данная
матрица визуально показывает статус задач.
##### 3.4 Список литературы
Данная вкладка позволяет внести книги, которые пользователь хочет прочесть.
Книгу можно добавить как вручную, так и с помощью csv-файлов.
При добавлении файла уже внесенные в список книги не удаляются. При сохранении в csv-файл в него сохраняются все книги,
которые есть на данный момент в списке.
### 4. Повторный вход
При повторном входе все данные сохраняются. Если какие-то данные не отобразились, следует нажать кнопку
обновления данных, например, "Обновить матрицу".