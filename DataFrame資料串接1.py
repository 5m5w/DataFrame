import pandas as pd

df1 = pd.DataFrame([['a',1],['b',2]], columns=['letter', 'number'])

df2 = pd.DataFrame([['c',3],['D',4]],columns=['letter','number'])

df3 = pd.DataFrame([['apple', 3.1],['banana', 4.2]], columns=['fruit', 'dollar'])

# 以上資料建立，必須特別注意使用[]，對於在同一列的數值，都必須被[]起來

df12 = pd.concat([df1, df2])
# 預設為縱向串接，也就是 axis=0，
print(df12)


df13 = pd.concat([df1, df3], axis=1)
# axis=1 為橫向串接
print(df3)

df14 = pd.concat([df1, df3])
# 因為縱向串接，但df1, df3並沒有相同的欄位名稱，所以是
print(df14)
#  letter  number   fruit  dollar
# 0      a     1.0     NaN     NaN
# 1      b     2.0     NaN     NaN
# 0    NaN     NaN   apple     3.1
# 1    NaN     NaN  banana     4.2

# 注意！串接的每一欄位，都必須是同一種的資料型態

print(df14['letter'])
# 顯示的是 object 資料型態
print(df14['number'])
# 顯示的是 float64 數值型態