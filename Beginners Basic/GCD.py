def Find_gcd(val):
    divisors =[x for x in range(1,val//2+2) if val%x==0]
    return max(divisors)
if __name__ =="__main__":
    val =int(input("Enter the number: "))
    print(f"The entered number's Greatest Common Divisor is {Find_gcd(val)}")