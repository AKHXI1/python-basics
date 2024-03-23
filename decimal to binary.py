decimal_number=int(input("enter the decimal number:"))
if decimal_number==0:
    print(0)
else:
    binary_number=""
    while decimal_number>0:
        reminder=decimal_number%2
        decimal_number=decimal_number//2
        binary_number=str(reminder)+binary_number
    print(binary_number)
