def CheckPrime(val):
    count =0
    for i in range(2,val//2+2):
        if val%i==0:
            count+=1
    if count==0:
        return "Prime number"
    return "not a Prime number"
if __name__=="__main__":
    val =int(input("Enter the number: "))
    print(f"The entered number {val} is {CheckPrime(val)}")