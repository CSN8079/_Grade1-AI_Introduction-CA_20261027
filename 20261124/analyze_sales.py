import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]  # 或 ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

# 读取清洗后的数据
df = pd.read_csv("sales_clean.csv")

# 计算每行总金额
df["总金额"] = df["价格"] * df["数量"]

# 按商品类别统计销售额，并降序输出
category_sales = df.groupby("商品类别")["总金额"].sum().sort_values(ascending=False)
print(category_sales)

# 画柱状图（使用英文标签，避免中文字体问题）
plt.figure(figsize=(8, 5))
plt.bar(category_sales.index, category_sales.values)
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales (yuan)")
plt.tight_layout()
plt.savefig("category_sales.png", dpi=100)
plt.show()

