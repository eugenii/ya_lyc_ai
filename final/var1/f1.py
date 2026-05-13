# base
import pandas as pd

file_name = input().strip()

data = pd.read_csv(file_name)

lines = len(data)

columns = len(data.columns)

avg_sleep_duration = data['Sleep duration'].mean()

median_sleep_efficiency = data['Sleep efficiency'].median()

print(
    lines,
    columns,
    round(avg_sleep_duration, 2),
    round(median_sleep_efficiency, 2), sep='\n'
)
