def Find_Common_Divisor(num1,num2):
    num1_divisors =[]
    num2_divisors =[]
    common_divisors =[]
    for i ,j in zip(range(1,num1//2+1) , range(1,num2//2+1)):
        if num1%i ==0:
            num1_divisors.append(i)
        if num2%j==0:
            num2_divisors.append(j)
    for k in num1_divisors:
        if i in num2_divisors:
            common_divisors.append(k)
    if common_divisors:
        return max(common_divisors)
    else:
        return 1
if __name__ =="__main__":
    number1 =int(input("Enter the number 1: "))
    number2 =int(input("Enter the number 2: "))
    print(f"The Greatest Common Divisor for the numbers {number1} and {number2} is {Find_Common_Divisor(number1,number2)}")