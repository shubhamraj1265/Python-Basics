number = int(input("Enter any number up to 5 digits: "))

if 0 <= number <= 9:
    print("It is Single digit number")
elif 10 <= number <= 99:
    print("It is Double digits number")
elif 100 <= number <= 999:
    print("It is Three digits number")
elif 1000 <= number <= 9999:
    print("It is Four digits number")
elif 10000 <= number <= 99999:
    print("It is Five digits number")
else:
    print("It is more than 5 digits number")
