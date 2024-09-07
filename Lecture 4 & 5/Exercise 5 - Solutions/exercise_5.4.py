# finding the week daya and weekend

day = int(input("Enter a number from 1 to 7 (1 for Sunday, 7 for Saturday): "))

if day < 1 or day > 7:
    print("Invalid input! Please enter a number between 1 and 7.")
else:
    if day == 6 or day == 7:
        print("It's a weekend.")
    else:
        print("It's a weekday.")
