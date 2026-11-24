import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 或 ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 读取清洗后数据
df = pd.read_csv("sales_clean.csv")

# 计算总金额
df["总金额"] = df["价格"] * df["数量"]

# 按支付方式汇总销售额，降序输出
payment_sales = df.groupby("支付方式")["总金额"].sum().sort_values(ascending=False)
print(payment_sales)

# 画柱状图：英文标签避免乱码



plt.figure(figsize=(8, 5))
plt.bar(payment_sales.index, payment_sales.values)
plt.title("按支付方式销售额")
plt.xlabel("支付方式")
plt.ylabel("销售额（元）")
plt.tight_layout()
plt.savefig("payment_sales.png", dpi=100)
plt.show()

