
#printing all number with verification

n=int(input("Enter n: "))

i=1
while i<=n:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")

    else:
        print(i)
    i+=1