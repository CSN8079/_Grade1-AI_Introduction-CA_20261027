
while True:
    bjb = 8
    a = int(input("请输入购买本数"))
    psf = 5
    money = bjb * a
    s = "应付金额为："
    if money >=30 :
        print(s+str(money)+"元")
    else:
        print(s+str(money + psf)+"元")

