# Function for Fibonacci number
# Fibunatcci numbers {0,\;1,\;1,\;2,\;3,\;5,\;8,\;13,\;21,\;34,\;55,\;89,\;144,....}
# Fibunatcci formula  F_{n}=F_{n-1}+F_{n-2}}
def F(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return F(n-1)+F(n-2)
   