list_new=[]
print("initial blank list")
print(list_new)
list_new.append(10)
list_new.append(20)
list_new.append(30)
print("value added list")
print(list_new)

ListA = [2, 4, 2, 6, 7, 2]
print(ListA.count(2)) #counts no. of times element appears
ListA.insert(2,50) #Insert object at specific index
print(ListA)
print(ListA.pop(2)) #Removes an element at the specified index
ListA.remove(2) #removes or deletes and element from the list
print(ListA)

ListA = [2, 4, 2, 6, 7, 2]
ListB = [100,200,300]
ListA.extend(ListB) #adds elements in a list to the end of another list
print(ListA)

ListA = [2, 4, 2, 6, 7, 2]
ListA.reverse() #Reverses the elements in the list
print(ListA)
ListA.sort() #Sorts the elements in the list
print(ListA)

List_A = [1, 3, 6, 2] + [5, 4, 7] #Concatenation
print (List_A)
print ("Max =", max(List_A)) #prints maximum value
print ("Min =", min(List_A)) #prints minimum value
print ("Sum =", sum(List_A)) #sum operation add the values in the list of numbers

first=[10,20,30]
second=first
print(first)
print(second)
first[1]=99
print(first)
print(second)