x=5

def function1():
    print("value in 1st function :",x)

def function2():
    global x
    x=555
    print("value in 2nd function:",x)

def function3():
    print("value in 3rd function :",x)

function1()
function2()
function3()