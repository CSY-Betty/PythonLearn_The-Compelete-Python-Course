import pandas as pd

eng = ['apple', 'banana', 'mango', 'watermelon']
chi = ['A', 'B', 'M', 'W']

dict = {'英文': eng, '開頭': chi}

df = pd.DataFrame(dict, index=['a', 'b', 'c', 'd'])

print(df)