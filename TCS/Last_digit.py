def Find_last_digit(num):
    return num%10
if __name__=="__main__":
    number=int(input("Enter the number: "))
    print(f"The last digit of the number {number} is {Find_last_digit(number)}")