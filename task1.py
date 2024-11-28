import random
def task1():
    array=list(map(int,input("Enter your steps count ").split()))
    
    
        
        
       
    array.sort(reverse = True)
    print("this array: ",array)
    print("highest step counts: ", min(array))
    print("lowest step counts: ",max(array))
    print("average daily step: ",sum(array)/len(array))
task1()

def random_input():
    array = [random.randint(1,100) for _ in range(30)]
    for _ in array:
        print(_,end=" ")
# random_input()


