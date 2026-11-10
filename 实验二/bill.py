price = 8
quantity = int(input("请输入购买本数："))
subtotal = price * quantity
delivery_fee = 5
total = subtotal + delivery_fee
print("小计：", subtotal, "元")
print("应付金额：", total, "元")