def Find_odd_even(val):
    if val & 1 == 0:
        return True
    return False
if __name__ =="__main__":
    number_list =int(input("Enter the number: "))
    if Find_odd_even(number_list):
            print(f"The entered number {number_list} is Even")
    else:
            print(f"The entered number {number_list} is Odd")
