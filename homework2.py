str = input("Enter a string: ")
i = 0
nums = 0
letters = 0
while i < len(str):
    if str[i] in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
        nums += 1
    elif str[i] in (" " , "," , ".", "?", "!", "/", ";", "`", "]", "[", "{", "}", "(", ")"): 
        nums += 1
        nums -= 1
    else:
        letters += 1
    i += 1
print("Numbers: ", nums)
print("Letters: ", letters)