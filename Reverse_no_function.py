def Reverse_String(String):
    reversed_string =""
    for char in String:
        reversed_string = char + reversed_string
    return reversed_string
if __name__ =="__main__":
    String =input("Enter the string :")
    print(f"The Reversed({String}) is",Reverse_String(String))