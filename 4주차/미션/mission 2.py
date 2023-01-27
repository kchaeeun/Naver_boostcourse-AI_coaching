from pandas import Series, DataFrame
import pandas as pd

df1 = DataFrame([
                 ["cherry","Fruit",100], #colums가 나올자리를 남겨줘야 한다!!
                 ["mango","Fruit",110],
                 ["potato","Vegetable",60],
                 ["onion","Vegetable",80]],
                 columns = ["Name","Type","Price"])
df2 = DataFrame([                     
                 ["pepper","Vegetable",50],
                 ["carrot","Vegetable",70],
                 ["banana","Fruit",90],
                 ["kiwi","Fruit",120]],
                 columns = ["Name","Type","Price"])

#df1, df2를 colums를 이용해 결합
df3 = pd.concat([df1,df2], axis = 0)

#fruit와 vegetable의 type에 따라 정렬하고, 가격을 내림차순으로 정리
df_fruit = df3.loc[(df3['Type']=='Fruit')]   #fruit만 일부만 쉽게 정렬
df_fruit = df_fruit.sort_values(by=['Price'], axis = 0, ascending = False)

df_veg = df3.loc[(df3['Type']=='Vegetable')]  #vegtable의 일부만 쉽게 정렬
df_veg = df_veg.sort_values(by=['Price'], axis = 0, ascending = False)

#fruit와 vegetable 상위 2개의 가격의 합을 출력
print('Sum of Top 2 Fruit Price : ', sum(df_fruit['Price'][0:2]))
print('Sum of Top 2 Vegetable Price : ', sum(df_veg['Price'][0:2]))
