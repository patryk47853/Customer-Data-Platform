import pandas as pd

df = pd.read_csv(
    "data/raw/Online_Retail.csv",
    encoding="ISO-8859-1"
)

print(df.head())