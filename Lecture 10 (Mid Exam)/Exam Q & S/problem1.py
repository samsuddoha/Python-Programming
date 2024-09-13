
# Taking the number of inputs
n = int(input("Enter how many numbers you want to input: "))
numbers = []

sum=0
for i in range(n):
    number = int(input(f"Enter number {i + 1}: "))
    sum+=number
    numbers.append(number)

# Finding the sum of the numbers
average = sum / n

# Removing duplicates using set which does not support duplicate and convert again into list
#final_list = list(set(numbers))

# Removing duplicates manually
final_list = []
for num in numbers:
    if num not in final_list:
        final_list.append(num)

# Printing the final results
print(f"Sum: {sum} and Average: {average:.2f}")
print(f"Final list without duplicates: {final_list}")
