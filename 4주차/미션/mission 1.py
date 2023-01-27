from pandas import Series
import pandas as pd

idx = ["HDD", "SSD", "USB", "CLOUD"]
data = [19, 11, 5, 97]

#위 데이터로 series를 구현해보세요.
series = Series(data = data, index = idx)

#10 이상 20 이하를 가지는 데이터만 이용해 다시 series를 정의하세요.
series = series[series>=10][series<=20]  # &(and) , |(or) 사용하면 더 빨라짐
print(series)
