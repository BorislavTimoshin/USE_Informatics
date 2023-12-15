import os

folders = [
    "10. Поиск символов в текстовом редакторе",
    "12. Выполнение алгоритмов для исполнителей",
    "13. Организация компьютерных сетей. Адресация",
    "14. Кодирование чисел. Системы счисления",
    "15. Преобразование логических выражений",
    "16. Рекурсивные алгоритмы",
    "17. Обработки числовой последовательности",
    "18. Робот-сборщик монет",
    "19. Выигрышная стратегия. Задание 1",
    "2. Построение таблиц истинности логических выражений",
    "20. Выигрышная стратегия. Задание 2",
    "21. Выигрышная стратегия. Задание 3",
    "22. Многопроцессорные системы",
    "23. Оператор присваивания и ветвления. Перебор вариантов, построение дерева",
    "24. Обработка символьных строк",
    "25. Обработка целочисленной информации",
    "26. Обработка целочисленной информации",
    "27. Программирование",
    "3. Поиск информации в реляционных базах данных",
    "5. Анализ и построение алгоритмов для исполнителей",
    "6. Определение результатов работы простейших алгоритмов",
    "8. Перебор слов и системы счисления",
    "9. Работа с таблицами"
]

# Пути задач, которые пока не получилось решить
unresolved_tasks = [

]

# Анализ информационных моделей
task_1 = [

]
# Кодирование и декодирование информации
task_4 = [

]
# Кодирование и декодирование информации. Передача информации
task_7 = [

]
# Вычисление количества информации
task_11 = [

]

""" Проверка на то, решался ли введенный номер ЕГЭ """

website = input()  # Решу ЕГЭ, Поляков, КЕГЭ
number_of_task = int(input())

if number_of_task in task_1:
    print("Файл существует - 1. Анализ информационных моделей")
    exit()
if number_of_task in task_1:
    print("Файл существует - 4. Кодирование и декодирование информации")
    exit()
if number_of_task in task_1:
    print("Файл существует - 7. Кодирование и декодирование информации. Передача информации")
    exit()
if number_of_task in task_1:
    print("Файл существует - 11. Вычисление количества информации")
    exit()

main_directory = "C:/Python_Projects/ЕГЭ_Информатика"

for folder_name in folders:
    directory_task = f"{main_directory}/{folder_name}"
    for folder in os.listdir(directory_task):
        if folder == website:
            directory_website = f"{directory_task}/{website}"
            for file in os.listdir(directory_website):
                if file.startswith(str(number_of_task)):
                    print(f"Файл существует - {directory_website}/{file}")
                    exit()
else:
    print("Файл не существует")
