import math
import sys
print("Investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")
user = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

if user == 'investment' or user == 'Investment' or user == 'INVESTMENT':
    user_deposit = int(input("Enter the deposit: "))
    interest_rate = int(input("Enter the interest: "))
    r = interest_rate/100
    years = int(input("Enter the no. of years: "))
    interest = input("Enter the simple interest or compound interest: ")
    # A = p*(1+r*t)
    if interest == "simple":
        si = user_deposit * (1 + r * years)
        print('Simple Interest: {0}'.format(si))
    # A = p*math.pow((1+r),t)
    elif interest == "compound":
        ci = user_deposit * math.pow((1+r), years)
        print('Compound Interest: {0}'.format(ci))
    else:
        print("Please enter valid interest type. Allowed values are simple/compound")
        sys.exit(1)

elif user == 'Bond' or user == 'bond' or user == 'BOND':
    house_value = int(input("Enter the present value of the house: "))
    interest_rate_bond = int(input("Enter the interest rate: "))
    i = (interest_rate_bond/100)/12
    number_of_months = int(input("Enter the number of months: "))
    repayment = (i * house_value)/(1 - (1+i) ** (-number_of_months))

    print('Money to be repay each month: {0}'.format(repayment))

else:
    print("Wrong, enter the 'investment' or 'bond'")



