#Lab 4: Task 4: List and For loop

#List
test_list=[1,2,3,4,2.5,'str1',"str2"]

print(test_list)
for i in range(0,len(test_list)):
    print(test_list[i])
    test_list[i]=i**3
print(test_list)
   

    
    