import pandas as pd
df = pd.read_csv('sales_data.csv')

print(df.head())

print("替换前：", df["支付方式"].value_counts())

df["支付方式"] = df["支付方式"].replace("微信", "微信支付")

print("替换后：", df["支付方式"].value_counts())

print("价格中位数：", df["价格"].median())
df["价格"] = df["价格"].fillna(df["价格"].median())
print("填充后缺失数：", df["价格"].isna().sum())
df.drop_duplicates(inplace=True)
print("删除重复后行数：", df.shape[0])
df.to_csv("sales_clean.csv", index=False)
df_check = pd.read_csv("sales_clean.csv")
print(df_check.shape)
print(df_check["支付方式"].value_counts())
print(df_check.duplicated().sum())
