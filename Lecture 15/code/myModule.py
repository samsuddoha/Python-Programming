def prime(num):
    if num<=1:
        return  False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

def sum_digit(num):
    sum=0
    while num!=0:
        sum+=int(num%10)
        num=int(num/10)
    return sum
