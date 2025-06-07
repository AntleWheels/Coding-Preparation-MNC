def CheckPrime(number):
    remainder =0
    for i in range(2,int(number**0.5)+1):
        if number%i ==0:
            remainder +=1
    if remainder ==0 and number >1:
        return "Prime"
    else:
        return "Not Prime"

if __name__ =="__main__":
    number =int(input("Enter a number to check: "))
    print(f"The entered number {number} is",CheckPrime(number))