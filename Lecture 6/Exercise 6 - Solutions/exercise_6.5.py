#finding the largest number from a list

numbers=[12, 23, 35, 10, 56, 30]

result = -1000
for n in numbers:
    if n>result:
        result=n
print(f"The largest numer is: {result}")
