#询问每个顾客要几个几个比萨，
#询问每个比萨单价
#计算比萨总金额
#计算销售税
#向用户显示应该支付的总价
number_of_pizzas = eval(input("How many pizzas do you want? "))

cost_per_pizza = eval(input("How much does each pizza cost?"))

subtotal = number_of_pizzas * cost_per_pizza

tax_rate = 0.08
sales_tax = subtotal * tax_rate

total = subtotal + sales_tax

print("The total cost is $",total)
print("This includes $",subtotal,"for the pizza and")
print("$",sales_tax,"in sales tax.")

