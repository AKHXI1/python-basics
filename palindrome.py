inputString=input("enter the string to check whether it is palindrome or not:")
inputString=inputString.upper()
if inputString==inputString[::-1]:
    print("the string is palindrome")
else:
    print("not palindrome")