
import pandas as pd

df = pd.read_excel("D:\HungND\Dataset\laokhoa_daxuly.xlsx", sheet_name='Dulieuso')
#print(df)
df.to_excel("D:\laokhoa_daxuly.xlsx", sheet_name='Dulieuso')

df.to_csv("D:\HungND\Dataset\laokhoa_daxuly.csv", header=True, index=False, encoding='utf-8')

df1= pd.read_csv("D:\HungND\Dataset\laokhoa_daxuly.csv", encoding='utf-8',sep = ',')
print("Danh sach sau ghi sang  csv")
print(df1)