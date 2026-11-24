# 热身示例：先读代码、预测结果，再运行。无需提交这个文件。
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager

folder = Path(__file__).resolve().parent

# 一、检查正式数据能否读取（这里只查看，不修改或覆盖原文件）
orders = pd.read_csv(folder / "sales_data.csv")
print("正式数据的行数、列数：", orders.shape)
print(orders.head())

# 二、用另一组“校园义卖”小数据学习方法
demo = pd.DataFrame({
    "摊位": ["文具摊", "文具摊", "零食摊", "零食摊", "文具摊"],
    "单价": [4, None, 6, 8, 4],
    "件数": [2, 1, 3, 2, 2],
    "付款": ["现金", "扫码", "扫码支付", "现金", "现金"],
})
print("\n热身原始数据：\n", demo)
print("缺失值数量：\n", demo.isna().sum())
print("付款写法：\n", demo["付款"].value_counts())
print("完全重复的行数：", demo.duplicated().sum())

# 三、处理数据：每一步运行前先预测会改变什么
demo["付款"] = demo["付款"].replace("扫码", "扫码支付")
demo["单价"] = demo["单价"].fillna(demo["单价"].median())
demo = demo.drop_duplicates()
print("\n处理后：\n", demo)
print("处理后的缺失数：", demo["单价"].isna().sum())
print("处理后的重复数：", demo.duplicated().sum())

# 四、计算、分组、核对
demo["金额"] = demo["单价"] * demo["件数"]
summary = demo.groupby("摊位")["金额"].sum().sort_values(ascending=False)
print("\n各摊位金额：\n", summary)
print("汇总合计：", summary.sum(), "明细合计：", demo["金额"].sum())
demo.to_csv(folder / "warmup_clean.csv", index=False, encoding="utf-8-sig")

# 五、生成图表：找不到中文字体时使用英文标签，方便不同电脑运行
preferred = ["Microsoft YaHei", "SimHei", "PingFang SC", "Noto Sans CJK SC", "WenQuanYi Zen Hei"]
installed = {item.name for item in font_manager.fontManager.ttflist}
chosen = next((name for name in preferred if name in installed), None)
if chosen:
    plt.rcParams["font.sans-serif"] = [chosen]
    labels, title, xlabel, ylabel = summary.index, "各摊位义卖金额", "摊位", "金额（元）"
else:
    names = {"文具摊": "Stationery", "零食摊": "Snacks"}
    labels = [names[name] for name in summary.index]
    title, xlabel, ylabel = "Sales by stall", "Stall", "Amount (CNY)"
    print("未找到中文字体，本示例使用英文图表标签。")
plt.bar(labels, summary.values)
plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.tight_layout()
plt.savefig(folder / "warmup_chart.png", dpi=150)
print("已保存 warmup_clean.csv 和 warmup_chart.png。")
# 如需弹出图表窗口，取消下一行开头的 # 号：
# plt.show()
plt.close()

# 练习：改成按“付款”分组，并同步调整图表标签。
# 正式任务请新建 clean_sales.py 和 analyze_sales.py，不要直接覆盖本示例。
