from pandas import Series, DataFrame
import pandas as pd

df1 = pd.DataFrame({'Name':['cherry','mango','potato','onion'],
                    'Type':['Fruit','Fruit','Vegetable','Vegetable'],
                    'Price':[100,110,60,80]})
df2 = pd.DataFrame({'Name':['pepper','carrot','banana','kiwi'],
                    'Type':['Vegetable','Vegetable','Fruit','Fruit'],
                    'Price':[50,70,90,120]})

#df1, df2를 colums를 이용해 결합
df3 = pd.concat([df1,df2], axis = 0)

#fruit와 vegetable의 type에 따라 정렬하고, 가격을 내림차순으로 정리
df_fruit = df3.loc[(df3['Type']=='Fruit')]   #fruit만 일부만 쉽게 정렬
df_fruit = df_fruit.sort_values(by=['Price'], ascending = False)

df_veg = df3.loc[(df3['Type']=='Vegetable')]  #vegtable의 일부만 쉽게 정렬
df_veg = df_veg.sort_values(by=['Price'], ascending = False)
print(df_veg)

#fruit와 vegetable 상위 2개의 가격의 합을 출력
print('Sum of Top 2 Fruit Price : ', sum(df_fruit['Price'][0:2]))
print('Sum of Top 2 Vegetable Price : ', sum(df_veg['Price'][0:2]))

