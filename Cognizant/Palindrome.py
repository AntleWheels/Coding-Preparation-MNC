def Check_Palindrome(String):
    check=""
    for char in String:
        check = char+check
    if check==String:
        return "'Plaindrome'"
    else:
        return "not a 'Palindrome'"
if __name__=="__main__":
    String = input("Enter the string to check plaindrome: ")
    print(f"The entered string{String} is",Check_Palindrome(String))