# 02 ИИиДедушка.
# import pandas as pd


# data = pd.read_csv('marks.csv')
# print(data.info())
# # data = pd.data.values
# data['mean'] = data.mean(axis=1)

# data.sort_values(by='mean', inplace=True)

# # Вычисляем средние значения
# first_5_mean = data['mean'].iloc[1:5].mean()  # первые 5 строк по порядку
# middle_mean = data['mean'].iloc[5:-5].mean()  # средние 5 строк по порядку
# last_5_mean = data['mean'].iloc[-5:].mean()   # последние 5 строк по порядку

# # Заменяем значения в колонке 'mean' для первых и последних 5 строк
# data.loc[data.index[:5], 'mean'] = first_5_mean
# data.loc[data.index[5:-5], 'mean'] = middle_mean   
# data.loc[data.index[-5:], 'mean'] = last_5_mean 

# print(round(first_5_mean, 3), round(middle_mean, 3), round(last_5_mean, 3), sep='\n')

f = open('marks.csv', 'r')
data = [i.strip().split(',') for i in f.readlines()]

data = data[1:]
avg_data = []
for line in data:
    avg = sum([int(i) for i in line]) / len(line)
    avg_data.append(avg)
avg_data.sort()
# print(avg_data)
first_5_mean = sum(avg_data[:5]) / 5
middle_mean = sum(avg_data[5:-5]) / len(avg_data[5:-5])
last_5_mean = sum(avg_data[-5:]) / 5
print(round(first_5_mean, 2), round(middle_mean, 2), round(last_5_mean, 2), sep='\n')