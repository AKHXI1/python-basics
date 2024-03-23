data='myprogram.exe'
print(data[2])
print(data[-1])
print(len(data))
print(data[0:8])

next
print(data[5:9])

index=data.rfind(".")
if data[index:]==".exe":
    data=data[:index]
print(data)

middle_name=(len(data)//2)
print(data[middle_name])