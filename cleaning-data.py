import pandas as pd


df = pd.read_csv('online_retail.csv')

# drops any duplicate row
df.drop_duplicates(inplace=True)

# fill missing CustomerID with 0
df['CustomerID'].fillna(0, inplace=True)

# fill missing Description with 'Description Not Available'
df['Description'].fillna("Description Not Available", inplace=True)

# filter out negative Quantity and UnitPrice
df = df[df['Quantity'] >= 0]
df = df[df['UnitPrice'] >= 0]

# convert 'InvoiceDate' to datetime and nvalid dates will be set to NaT with 'coerce'
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'], errors='coerce')

# trim leading/trailing spaces in 'Description' column and ensure a consistent format
df['Description'] = df['Description'].str.strip().str.upper()

def normalize_stock_code(stock_code):
    stock_code = stock_code.strip()
    length = len(stock_code)
    
   
    if length == 5:
        return stock_code
    elif length > 5:
        # trim to the first 5 digits if longer
        return stock_code[:5]
    else:
        # if it's not numeric or shorter than 5 digits return n/a
        return 'N/A'

df['StockCode'] = df['StockCode'].apply(normalize_stock_code)

# summary of missing values after cleaning
print("Missing values after cleaning:\n", df.isnull().sum())

# save the cleaned dataset to a new CSV file
df.to_csv('cleaned-online-retail.csv', index=False)

print("Data cleaning completed and saved as 'cleaned-online-retail.csv'.")
