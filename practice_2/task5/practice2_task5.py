import pandas as pd
import collections
import json
import os

df = pd.read_csv("Accidental_Drug_Related_Deaths_2012-2022.csv", low_memory=False)
data = df[['Age', 'Sex', 'Race', 'Death City', 'Location', 'Location if Other', 'Cause of Death']].head(None)
# print(data)

result = list()

pd.set_option('display.float_format', '{:.2f}'.format)
result.append({
    "Age max": int(df['Age'].max()),
    "Age min": int(df['Age'].min()),
    "Age mean": round(float(df['Age'].mean()), 1),
    "Age sum": int(df['Age'].sum()),
    "Age std": round(float(df['Age'].std()), 1)
    })

# print(result)

result.append(collections.Counter(df['Sex']))
result.append(collections.Counter(df['Race']))
result.append(collections.Counter(df['Death City']))
result.append(collections.Counter(df['Location']))
result.append(collections.Counter(df['Location if Other']))
result.append(collections.Counter(df['Cause of Death']))

# print(result)

# Сохраняем полученный результат в json
with open("result.json", "w") as file:
    file.write(json.dumps(result))

# Сохраняем ИСХОДНЫЙ набор данных в разные форматы
# Поддержка msgpack в pandas удалена с версии библиотеки 1.0.0
# Пересохранить DataFrame в msgpack не получится

with open("DrugDeaths.json", "w") as file:
    file.write(df.to_json(orient='split'))

df.to_pickle('DrugDeaths.pkl')

print(f"csv     = {os.path.getsize('Accidental_Drug_Related_Deaths_2012-2022.csv')}")
print(f"json    = {os.path.getsize('DrugDeaths.json')}")
# print(f"msgpack = {os.path.getsize('DrugDeaths.msgpack')}")
print(f"pkl     = {os.path.getsize('DrugDeaths.pkl')}")
