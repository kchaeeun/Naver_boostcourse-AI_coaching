from pandas import Series, DataFrame
import pandas as pd
import numpy as np

idx = ["Sue","Ryan","Jay","Jane","Anan"]
col = ["round_1","round_2","round_3","round_4","round_5"]
data = [[55,65,60,66,57],
        [64,77,71,79,67],
        [88,81,79,89,77],
        [45,35,30,46,47],
        [91,96,90,97,99]]

#위 데이터를 이용해 dataframe을 구성해보세요.
df = DataFrame(data, columns=col,index=idx)

#df에 새로운 column인 round_6의 데이터 [11,15,13,17,19]를 추가해보세요.
col_round_6 = Series([11,15,13,17,19],index=idx)
df['round_6']=col_round_6
print(df)

#각 데이터의 mean, max, min 값을 구해 출력해보세요.
idx2 = ["mean","max","min"] 
df2 = df.describe().loc[idx2] #**loc[], 대괄호값에 여러개를 넣어주고 싶으면 먼저 idx를 선언해줄것
print(df2)

a=df.describe()
print(a)




