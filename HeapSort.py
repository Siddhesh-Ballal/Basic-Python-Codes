def Swap(a,b):
    a,b = b,a

def Max_Heapify(List, i):
    Largest = i
    LeftChild = 2 * i 
    RightChild = 2 * i + 1
    while LeftChild <= len(List) and List[i] < List[LeftChild]:
        Largest = LeftChild
    while RightChild <= len(List) and List[i] < List[RightChild]:
        Largest = RightChild
    
    if Largest != i:
        Swap(List[i], List[Largest])
        Max_Heapify(List, Largest)

def HeapSort(List):
    for i in range(len(List)//2, 0, -1):
        Max_Heapify(List, i)
    for i in range(len(List), 0, -1):
        Swap(List[1], List[i])
        Max_Heapify(List, 1)


List = [9,5,4,1,3,6,2,8,7]
HeapSort(List)
print("Sorted List is: ", List)