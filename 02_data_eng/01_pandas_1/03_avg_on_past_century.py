# Среднее за ХХ век

count = int(input())

films = [input() for _ in range(count)]
delim = [";", ","]["," in films[0]]  # если в строке есть ",", то 1, т. е. разделитель delim[1]
raitings = [float(film.split(delim)[2]) for film in films if 1900 < int(film.split(delim)[1]) < 2001]
avg_raiting = sum(raitings) / len(raitings)
print(round(avg_raiting, 3))

# sample input:
# 12
# Побег из Шоушенка;1994;9.111
# 1+1;2011;8.807
# Начало;2010;8.662
# Леон;1994;8.681
# Бойцовский клуб;1999;8.645
# Иван Васильевич меняет профессию;1973;8.782
# Жизнь прекрасна;1997;8.624
# Достучаться до небес;1997;8.629
# Крестный отец;1972;8.732
# Криминальное чтиво;1994;8.619
# Назад в будущее;1985;8.626
# Тайна Коко;2017;8.608

# sample output:
# 8.717