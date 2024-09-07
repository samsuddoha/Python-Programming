#  generate multiplication table of a given number

n = int(input("Enter a number to print its multiplication table: "))

i=1
while i<=10:
    result=n*i
    print(f"{n} x {i} = {result}")
    i+=1


