def Find_factorial(num):
    factorial =1
    for i in range(1,num+1):
        factorial *=i
    return factorial

if __name__ =="__main__":
    num =int(input("Enter the number: "))
    print(f"The factorial of {num} is",Find_factorial(num))