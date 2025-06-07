def Reverse_Integer(num):
    reversed_num = 0
    while num>0:
        reversed_num = reversed_num*10 + num%10
        num //=10
    return reversed_num
if __name__=="__main__":
    num = int(input("Enter the number: "))
    print(f"The reversed form for the {num} is",Reverse_Integer(num))