#Lab 5: Task 1: Functions 

#single input and single output
def square(x):
    #y=x**2
    #return y
    return x**2
    
sq1=square(3)
inp=5
sq2=square(inp)
print('answer is  :',sq1)
print(sq2)
print(square(8))

#multiple input and multiple output
def addsub(x,y):
    add=x+y
    sub=x-y
    return add,sub

print(addsub(4,5))
answer=addsub(2,1)
print(answer)
print(answer[0])
print(answer[1])
ans1,ans2=addsub(5,6)
print(ans1)
print(ans2)

    
#HW Task 1: Explain the steps in the code above