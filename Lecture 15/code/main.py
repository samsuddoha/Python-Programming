import myModule as m
#taking a list as input

numbers=list(map(int, input("Enter numbers: ").split()))

sum_prime=0
for n in numbers:
    if m.prime(n):
        sum_prime+=n
if sum_prime==0:
    print("There is no prime numebr in the list")
else:
    digit_sum=m.sum_digit(sum_prime)
    if m.prime(digit_sum):
        print(f"The final sum {digit_sum} is a Prime")
    else:
        print(f" the final sum {digit_sum} is not Prime")