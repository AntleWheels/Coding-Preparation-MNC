def Find_odd_or_even(num):
    if num &1 == 0:
        return"Even"
    else:
        return "Odd"
if __name__=="__main__":
    number =int(input("Enter the number: "))
    print(f"The entered number {number} is {Find_odd_or_even(number)}")