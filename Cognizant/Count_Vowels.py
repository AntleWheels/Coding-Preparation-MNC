def Count_Vowels(String):
    vowels=["a","e","i","o","u"]
    count =0
    for char in String:
        if char in vowels:
            count+=1
    return count
if __name__=="__main__":
    String =input("Enter the string: ")
    print("There are",Count_Vowels(String.lower().strip()),f"in the string {String}.")