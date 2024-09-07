# Factorial of number n

n = int(input("Enter a number for factorial: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    i=1
    fact = 1
    while i<=n:
        fact*=i
        i+=1
    print(f"The factorial of {n} is: {fact}")
