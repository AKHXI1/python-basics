squares=[]
for x in range(10):
    squares.append(x**2)
print(squares)

comb=[]
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            comb.append((x,y))
print(comb)

