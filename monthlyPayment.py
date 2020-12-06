# @Author  : Vijayalakshmi K @Time    : 12/2/2020 8:22 PM

import math

print('Enter the Loan Amount: ')
loan = input()
loanAmt = float(loan)

print("Enter the Interest Rate: ")
ir = input()
iRate = float(ir)
valIR = (iRate/100)*12

print("Enter the number of Years: ")
yr = input()
year = float(yr)

comR = 1 + (iRate/100)
comYr = year * 12
compPow = pow(comR, comYr)

# Compute the Monthly Payment
monthlyPmt = ((loanAmt * (iRate/100)) / (1 - (1 / compPow)))
print('The Monthly Payment is {}'.format(monthlyPmt))
# loan amount*monthlyinteresrate/(1-(1\1+monintrate^pow of nof years*12
#payMonthly = loanAmt * (valIR * (pow(1 + valIR,year)) / (pow((1 + valIR),year) - 1))