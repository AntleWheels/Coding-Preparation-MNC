def Armstrong(val):
    length =len(val)
    check=0
    for i in val:
        check+=int(i)**length
    if check == val:
        return "is Armstrong"
    return "is not an Armstrong"
if __name__ =="__main__":
    val = input("Enter the number: ")
    print(f"The entered number {val} {Armstrong(val)}")