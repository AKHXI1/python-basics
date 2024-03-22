def addition(*numbers):
    total=0
    for no in numbers:
        total=total+no
    print("sum is ",total)
addition()
addition(10,5,3,2,6)
addition(54,2.5,1,5)