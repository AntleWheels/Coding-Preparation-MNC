def Count_digits(val):
    count =0
    for i in val:
        count +=1
    return count
if __name__ =="__main__":
    val =input("Enter the number: ")
    print(f"There are {Count_digits(val)} numbers in {val}")