def whereismymoney(hours, rate):
    if hours <= 40:
        pay=(hours*rate)
    # Ben Schweighauser
    # Syntax error #1: extra parentheses in else statement
    else:
        pay=(((40*rate)+(hours-40)*(rate*1.5)))
    return pay
try:
    a=float(input("How many hours did you work?\n"))
    b=float(input("What is your rate per hour?\n"))
    totalpay=whereismymoney(a, b)
    # Ben Schweighauser
    # Syntax error #2: spelling error
    print('Your total pay is $',totalpayment)
# Ben Schweighauser
# Syntax error #3: input not numeric (no way to exit if input isn't a number)
#except:
    #print('Please enter a number')
# Code should output the total payment for the number of hours worked