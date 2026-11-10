
R, B, G, Y, C, M, W, N = "\033[0m", "\033[1m", "\033[92m", "\033[93m", "\033[96m", "\033[95m", "\033[97m", "\033[44m"

def tp(s, c=R):
    for ch in s:
        print(c + ch + R, end="", flush=True)
    print()

tp(f"{C}{B}╔══════════════════════════════╗\n║  📚 图 书 购 买 系 统  📚  ║\n╚══════════════════════════════╝{R}", C)

price = 8
print(f"{Y}💰 单价：{G}{B}{price} 元/本{R}")

while True:
    try:
        q = int(input(f"{C}🛒 请输入购买本数：{R}"))
        if q >= 0: break
        print(f"{Y}⚠️ 不能为负数！{R}")
    except ValueError:
        print(f"{Y}⚠️ 请输入整数！{R}")

sub = price * q
fee = 5 if q else 0
total = sub + fee

print(f"{M}{'═'*32}{R}")
print(f"{W}{N}{B}       🧾  购 物 小 票  🧾       {R}")
print(f"{M}{'═'*32}{R}")
print(f"  📖 本数：{B}{q}{R} 本")
print(f"  💵 单价：{B}{price}{R} 元")
print(f"{M}{'─'*32}{R}")
print(f"  🧮 小计：{Y}{B}{sub}{R} 元")
print(f"  🚚 运费：{Y}{B}{fee}{R} 元")
print(f"{M}{'─'*32}{R}")
print(f"  💳 {G}{B}应付：{total} 元{R}")
print(f"{M}{'═'*32}{R}")

tp(f"{C}🌟 感谢购买，祝您阅读愉快！👋{R}", C)