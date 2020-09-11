from decimal import *
getcontext().prec = 100000

def nilakantha(reps):
        result = Decimal(3.0)
        op = 1
        n = 2
        for n in range(2, 2*reps+1, 2):
                result += 4/Decimal(n*(n+1)*(n+2)*op)
                op *= -1
        return result
print("Calculate value of Pi using this tool made by Gagan Arora!")
print("How many decimals?")
decimals = int(input())
print(nilakantha(decimals))
print("Thanks for using this tool!")