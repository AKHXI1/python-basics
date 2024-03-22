s=input("enter the string:")
for letter in s:
    print(letter)
    if letter=='a' or letter=='i':
        break
    print("out of the loop")