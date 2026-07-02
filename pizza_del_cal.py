name = input('what is you name: ')
cpizzas = input('how much pizzas do you want? ')
price = 24
stot = price * int(cpizzas)
if stot >= 50:
    stot = float(stot) * 0.9
else:
    stot = stot
dev = input('do you want delivry?: ')
if dev == 'yes':
    devp = 5.99
else:
    devp = 0
total = ((stot*1.15) + devp)
print()
print("========== RECEIPT ==========")
print("Customer:", name)
print("-----------------------------")
print("Pizzas:         ", cpizzas)
print("Price each:     $", round(price, 2))
print("Subtotal:       $", round(stot, 2))
print("Discount:      -$", round(10.11, 2))
print("Delivery:       $", round(devp, 2))
print("Tax:            $", round(15.33, 2))
print("-----------------------------")
print("TOTAL:          $", round(total, 2))
print("=============================")
print("Thank you for your order!")