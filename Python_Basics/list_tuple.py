#Lab 4: Task 3: List and Tuple

#List
test_list=[1,2,3,4,2.5,'str1',"str2"]
print(test_list)

print(test_list[3])
print(type(test_list[3]))
print(type(test_list))
test_list[2]='another string'
test_list[6]=3.4
print(test_list)
print(test_list[2])

#Tuple
test_tuple=(2,45,21,'str')
print(test_tuple[2])
#test_tuple[2]=44   #not allowed
print(type(test_tuple))

test_tuple=44  #This will destroy the tuple and assign an integer value in that variable
print(test_tuple)
print(type(test_tuple))


