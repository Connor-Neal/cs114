print('')
print('$=+=+=+==$ Welcome $==+=+=+=$')
print('')
print('How many coins do you want to despense')
print('')
coins = int(input())
dollars=coins//100
coins=coins-dollars * 100
quarters=coins//25
coins=coins-quarters * 25
dimes=coins//10
coins=coins-dimes * 10
nickels=coins//5
coins=coins-nickels * 5
pennies=coins
print('')
print("Dollars: ",dollars)
print("Quarters: ",quarters)
print("Dimes: ",dimes)
print("Nickels: ",nickels)
print("Pennies: ",pennies)
print('')
