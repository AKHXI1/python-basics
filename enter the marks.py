marks=int(input("Enter the marks:"))
if(marks>=90 and marks<=100):
    print("O grade")
elif(marks>=80 and marks<=89):
    print("A+ grade")
elif(marks>=70 and marks<=79):
    print("A grade")
elif(marks>=69 and marks<=60):
    print("B+ grade")
elif(marks>=59 and marks<=50):
    print("B grade")
elif(marks>=49 and marks<=40):
    print("C grade")
else:
    print("failed")