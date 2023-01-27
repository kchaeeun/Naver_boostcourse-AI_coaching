#Quiz 2
from pandas import Series, DataFrame
import pandas as pd

df1 = pd.DataFrame({'Name':['cherry','mango','potato','onion'],
                    'Type':['Fruit','Fruit','Vegetable','Vegetable'],
                    'Price':[100,110,60,80]})
df2 = pd.DataFrame({'Name':['pepper','carrot','banana','kiwi'],
                    'Type':['Vegetable','Vegetable','Fruit','Fruit'],
                    'Price':[50,70,90,120]})

df3 = pd.concat([df1,df2])
print(df3)

df_fruit= df3.sort_values(['Price'], ascending = False)[0:4]
df_veg = df3.sort_values(['Price'], ascending = False)[4:9]
print(df_fruit)
print(df_veg)
print('Sum of Top 2 Fruit Price:', sum(df_fruit["Price"][0:2]))
print('Sum of Top 2 Vegetable Price:', sum(df_veg["Price"][0:2]))
