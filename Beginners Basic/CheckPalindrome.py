number =(input("Enter the number: "))
if int(number) < 10:
    print(f"The number {number} is below 10")
elif(number==number[::-1]):
    print(f"The entered number is Plaindrome")
else:
    print("The number is not a palindrome")