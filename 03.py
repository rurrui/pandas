import pandas as pd

df = pd.read_excel('D:/Temp/output2.xlsx',index_col='ID')
print(df)
print(df.columns)