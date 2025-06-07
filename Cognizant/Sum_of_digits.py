def Sum_of_digits(digit):
    total = 0
    while digit>0:
        total += digit %10
        digit =digit //10
    return total

if __name__=="__main__":
    digit = int(input("Enter the number: "))
    print(f"The sum of digits in the {digit} is",Sum_of_digits(digit))