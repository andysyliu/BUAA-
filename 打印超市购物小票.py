#打印购物小票
total_amount = 0.0
name1 = input()
quantity1 = int(input())
price1 = float(input())

name2 = input()
quantity2 = int(input())
price2 = float(input())

total_price1 = quantity1 * price1
total_price2 = quantity2 * price2
total_amount = total_price1 + total_price2

print("-------------购物清单-------------",end="\n")
print("名称\t","数量\t","单价\t","总计",end="\n")
print(name1,"\t",quantity1,"\t",price1,"\t",total_price1,end="\n")
print(name2,"\t",quantity2,"\t",price2,"\t",total_price2,end="\n")

print("收款","\t\t\t",total_amount,end="")
#print(f"{total_amount}")