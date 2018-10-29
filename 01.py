import pandas as pd

df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['wzh', 'rurui', 'whvihs']})
df = df.set_index('ID')
df.to_excel(r'D:\temp\output.xlsx')
print('Done')
