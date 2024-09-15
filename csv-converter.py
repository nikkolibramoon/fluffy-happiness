import pandas as pd

# load excel file and covert it in csv file
excel_file = 'Online Retail copy.xlsx'
df = pd.read_excel(excel_file)
df.to_csv('online_retail.csv', index=False)
