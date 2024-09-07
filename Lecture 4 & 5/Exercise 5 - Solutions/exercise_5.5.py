# admission fee generation

age = int(input("Enter your age: "))

if age < 3:
    admission_fee = "Free admission"
elif age>=3 and age <= 12:
    admission_fee = "Tk. 500"
elif 13 <= age <= 20:  # this can be written in short for without using and
    admission_fee = "Tk. 2000"
else:
    admission_fee = "Tk. 5000"

print(f"The admission price is: {admission_fee}")
