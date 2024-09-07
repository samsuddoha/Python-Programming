
#problem 3: simple calculator

number1=float(input("Enter the first number: "))
number2=float(input("Enter the second number: "))

operator=input("Enter operator(+, -, *, /): ")

if operator=="+":
    result=number1+number2
    print(f"Sum of {number1} and {number2} is: {result}")
elif operator=="-":
    result = number1 - number2
    print(f"Difference of {number1} and {number2} is: {result}")
elif operator=="*":
    result = number1 * number2
    print(f"Product of {number1} and {number2} is: {result}")
elif operator=="/":
    if number2!=0:
        result = number1 / number2
        print(f"Division of {number1} and {number2} is: {result}")
    else:
        print(f"Undefined as the divisor is: {number2}")