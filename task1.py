import random
def task1():
    array=list(map(int,input("Enter your steps count ").split()))
    
    
        
        
       
    array.sort(reverse = True)
    print("this array: ",array)
    print("highest step counts: ", min(array))
    print("lowest step counts: ",max(array))
    print("average daily step: ",sum(array)/len(array))
task1()


