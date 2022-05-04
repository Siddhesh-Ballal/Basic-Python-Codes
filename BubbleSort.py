# Check every adjacent element;
# if Arr[i] > Arr[i+1], Swap the two.
# After each iteration you find subsequent index from the end having corect elemnt at place 
# Outer Loop i: from Len-1 -> 0
# Inner Loop j: from 0 -> i

def BubbleSort(List):
    for i in range(len(List)-1,0,-1):
        for j in range(i):
            if List[j]>List[j+1]:
                List[j], List[j+1] = List[j+1], List[j]
    return List

# Main:
List = eval(input("Enter the list in standard list format: "))
print("Sorted List is: ",BubbleSort(List))