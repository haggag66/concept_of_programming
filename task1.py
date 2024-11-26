import random
def task1():
    array=[]
    
    
    for i in range(3):
        number=int(input("enter step count today:"))
        array.append(number)
        
       
    array.sort(reverse = True)
    print("this array: ",array)
    print("highest step counts: ", min(array))
    print("lowest step counts: ",max(array))
    print("average daily step: ",sum(array)/len(array))
task1()


