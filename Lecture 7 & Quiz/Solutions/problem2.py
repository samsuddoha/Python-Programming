
#problem 2: Trainig program seat reservation program

name=input("Enter your name: ")
tokenNumber=int(input("Enter your token number: "))

if tokenNumber%2==1:
    print(f"{name}: your seat is confirmed.")
elif tokenNumber%2==0:
    print(f"{name}: you are in the waiting lits.")
elif tokenNumber==0:
    print(f"Sorry! {name}: No seat available for you.")