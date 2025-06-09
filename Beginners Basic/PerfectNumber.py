def CheckPerfect_number(val):
    divisors =[x for x in range(1,val//2+2) if val%x ==0]
    count =0
    for i in divisors:
        count+=i
    if count==val:
        return "Perfect number"
    return "not a Perfect number"
if __name__ =="__main__":
    val =int(input("Enter the number: "))
    print(f"The entered number {val} is {CheckPerfect_number(val)}")