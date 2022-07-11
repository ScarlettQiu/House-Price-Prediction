import pandas as pd


df = pd.read_csv(r'/Users/qiuyu/Desktop/ALY 6020/6020 dataset/6020 Project/Nashville_housing_data_2013_2016.csv')

df.info()

a = df.head()

b = df.describe()

print(a)

print(b)