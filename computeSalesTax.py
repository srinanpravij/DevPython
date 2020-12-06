# @Author  : Vijayalakshmi K @Time    : 12/2/2020 7:51 PM

print("Enter the amount:")
val = input()
cost = float(val)
taxedCost = cost * (8.875/100)
roundTax = round(taxedCost,2)
print('The purchase is ${} and the tax is ${}'.format(cost , roundTax))


