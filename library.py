# Function for Fibonacci numbers
# If you observe the below Python Fibonacci series pattern, First Value is 0, Second Value is 1,
#  and the following number is the result of the sum of the previous two numbers. 
# For example, Third value is (0 + 1), Fourth value is (1 + 1) so on.

# **********Fibonacci series pattern************
# {0,\;1,\;1,\;2,\;3,\;5,\;8,\;13,\;21,\;34,\;55,\;89,\;144,....}

# Fibunatcci formula  F_{n}=F_{n-1}+F_{n-2}}
# To get the Fibunatcci of (4) we should knows the Fibunatcci of
#  (3)and (2) and so on..

def fibunatcci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
# here I'm using a method call a (recursion) 
# where the solution depends on solutions to smaller instances of the same problem
        return fibunatcci(number-1)+fibunatcci(number-2)
# Fibunatcci of 0 is 0
# Fibunatcci of 1 is 1
# based on Fibunatcci of 2 and 1 we can get the Fibunatcci of 2 ,3 ,4 etc..

