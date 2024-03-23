binary_number=input("enter the binary number:")
decimal_number=0
exponent=len(binary_number)-1
for digit in binary_number:
    decimal_number=decimal_number+int(digit)*(2**exponent)
    exponent=exponent-1
print("the decimal equivalent is:",decimal_number)