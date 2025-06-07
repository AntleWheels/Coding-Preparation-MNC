def Count_digit(number):
    count=0
    while number>0:
        number =number//10
        count +=1
    return count
if __name__ =="__main__":
    number =int(input("Enter the numer: "))
    print(f"The number {number} has {Count_digit(number)}")