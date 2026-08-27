# samples from lesson
import pandas as pd

import matplotlib.pyplot as plt

# Гистограмма
grades = [5, 4, 5, 3, 4, 5, 4, 5, 3, 4]
plt.hist(grades, bins=5) # bins — сколько "корзинок" (интервалов) сделать
plt.xlabel("Оценка")
plt.ylabel("Количество учеников")
plt.title("Распределение оценок по математике")
plt.show()

# Столбчатая диаграмма
languages = ["Python", "C++", "Java", "JavaScript"]
students_count = [15, 4, 3, 6]

plt.bar(languages, students_count)
plt.xlabel("Язык программирования")
plt.ylabel("Количество учеников")
plt.title("На каких языках уже программировали ученики")
plt.show()

# Линейная диаграмма
weeks = [1, 2, 3, 4]
tasks_solved = [5, 8, 10, 12]
plt.plot(weeks, tasks_solved)
plt.xlabel("Неделя")
plt.ylabel("Количество решённых задач")
plt.title("Прогресс по количеству решённых задач")
plt.grid(True) # сетка, чтобы проще было ориентироваться
plt.show()

'''Графики появляются по очереди! сначала первый, потом второй - после ЗАКРЫТИЯ первого и т. д.'''

# Сначала получаем данные и подсчитываем по годам.

df = pd.read_csv('../data/kinopoisk-top250.csv')

films_per_year = df["year"].value_counts().sort_index()
films_per_year.value_counts()

plt.figure(figsize=(10, 6))
films_per_year.plot(kind="bar")
plt.xlabel("Год выпуска")
plt.ylabel("Количество фильмов")
plt.title("Количество фильмов топ-250 по годам")
plt.show()