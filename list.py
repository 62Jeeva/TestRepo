#slicing operation

numbers1=[10,20,30,40,50,60,70,80,90,100]
print(numbers1[:8])
print(numbers1[1:])
print(numbers1[::2])
print(numbers1[::3])
print(numbers1[::-1])  # prints in reverse order
print(numbers1[::2])
print(numbers1)
numbers1[5]=35 # reassigning the value in the list
print(numbers1)


# adding elements in the list
numbers2=[10,20,30,40,50,60,70,80,90,100]
print(numbers2)
print.append(1000) #will add the item in the last position
print.insert(3,200) # used to insert vlue in the given particular index position
print.extend([400,30,122]) #add the multiple values in the end of list
print(numbers2)

# removing elements from the list

numbers2.remove(1000) # remove the elements by value
print(numbers2)

numbers2.pop() # used to remove last element in the list
print(numbers2)

numbers2.pop(2) #used to remove value based on the index
print(numbers2)

del numbers2[5] # delete the value based in index value, del is a keyword
print(numbers2)

#