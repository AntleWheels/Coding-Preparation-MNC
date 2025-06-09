number = int(input("Enter the number: "))
divisors =[x for x in range(1,int(number//2)+2) if number%x ==0]
print(f"The divisors of {number} are {', '.join (map(str, divisors))}")