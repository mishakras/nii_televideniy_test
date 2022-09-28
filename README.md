# nii_televideniy_test
Реализация тестового задания для НИИ телевидения.
Описание задания:
При помощи фреймворков Flask и Bootstrap создать веб-страницу, которая будет динамически отображать переменную из бэкенда. Переменную менять в бэкенде раз в секунду с помощью функции случайного числа (0, 100). 

Как будет выглядеть и проверяться данное задание:
1) Реализация части бэкэнда. На языке Python 3 реализовать консольное приложение (либо же графическое приложение с использованием Tkinter), которое запустит генератор случайного числа и будет менять перемеменную, которая будет отображаться в web-браузере.
2) Реализация части фронтэнда. Запустить web-браузер и в разработаной HTML-странице, которая запуститься при старте фреймворка Flask, наблюдать динамическое изменение переменной в диапазоне от 0 до 100.

Инструкция по запуску:
  Для запуска бекэнда запустить командную строку в корневой папке проекта. Затем запустить команду *python main.py*. Запустится консольное приложение, которое будет выводить случай1ное число в строку и ждать подключения фронтенда для передачи ему данных.
  Для запуска фронтенда запустить еще одну командную строку в корневой папке проекта. Затем запустить команду *flask --app flaskr --debug run*. Затем перейти по адресу, который flask выведет в командной строке. У меня это  http://127.0.0.1:5000. Там откроется страница с выводом случайного числа.