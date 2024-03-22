num=int(input("Enter an number:"))
if(num==0):
    print("factorial of num is 1")
f=1
for i in range(1,num+1):
        f=f*i
print("factorial of",num,"is",f)