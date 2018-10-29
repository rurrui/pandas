import pandas as pd

df = pd.read_excel(r'D:\Temp\output.xlsx', header=None)
df.columns = ['ID', 'Name']
df.set_index('ID', inplace=True)
df.to_excel(r'D:\Temp\output2.xlsx')
print(df.columns)
