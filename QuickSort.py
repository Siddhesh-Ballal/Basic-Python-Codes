# DIVIDE AND CONQUER
# 1. Choose a Pivot element (Either last element or at Random)
# 2. Store (elements < pivot) in left sub-array, and (elements > pivot) in right sub-array
# 3. a) Call recursive QuickSort on Left Sub-array
#    b) Call recursive QuickSort on Right Sub-array

# We basically put pivot element at correct index of Sorted array 
# and continue the same for all elements recursively

# Take 2 pointer/indicators: i&j
# i searches for elements > pivot and j searches for elements < pivot
# i moves leftwards, j moves rightwards

# Swap i and j and continue till j is left of (or same as) i
# At this point, swap pivot and i
# Recursively Call Quicksort on Left and Right Sub-arrays   




def Partition(List, Left, Right):
    i = Left
    j = Right-1
    Pivot = List[Right]
    while i < j:
        while i < Right and List[i] < Pivot:
            i+=1
        while j > Left and List[j] >= Pivot:
            j-=1
        if i<j:
            List[i], List[j] = List[j], List[i]
    
    if List[i] > Pivot:
        List[Right], List[i] = List[i], List[Right]
    
    return i


# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right of pivot


def QuickSort(List, Left, Right):
    if Left < Right:
        PartitionIndex = Partition(List, Left, Right)
        QuickSort(List, Left, PartitionIndex-1)
        QuickSort(List, PartitionIndex+1, Right)

# Main:
List = eval(input("Enter the list in standard list format: "))
QuickSort(List, 0, len(List)-1)
print("Sorted List is: ", List)
