# Python 练习：先预测输出，再运行核对。
# 在终端中运行整个文件：python python_warmup.py
# 如果上次使用的是 python3 或 py，就沿用该命令。

# 示例一：用变量计算复印费用
pages = 10             # 复印页数
price_per_page = 2     # 每页价格（元）
total = pages * price_per_page
print("复印费用（元）：", total)

# 练习：只把 pages 改成 15。预测费用，再运行核对。

# 示例二：用 if/else 判断借书是否超期
days = 7              # 已借天数
limit = 7             # 最长可借天数

if days > limit:
    print("已超期")
else:
    print("未超期")

# 练习：只把 days 改成 8。预测输出，再运行核对。
# 观察：if 和 else 行末有冒号，分支里的 print() 向右缩进。
