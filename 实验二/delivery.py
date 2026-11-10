while True:
    bjb = 8
    a = int(input("请输入购买本数"))
    fee = 5
    money = bjb * a
    free_limit = 30
    s = "应付金额为："
    if money >= free_limit :
        print(s+str(money)+"元")
    else:
        print(s+str(money + fee)+"元")

