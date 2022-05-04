# Select Min val by traversing entire Unsorted List
# Place it at start of Unsorted List
# Continue doing same with remaining rest of the Unsorted List
# You are dividing the List as Sorted and Unsorted:

#           Sorted | Unsorted

def SelectionSort(List):
    for i in range(len(List)-1):                                # i: 0 -> Len-1
        Min = i
        for j in range(i, len(List)):                           # j: i -> Len    
            if List[j]<List[Min]:
                Min = j          
        List[Min], List[i] = List[i], List[Min]
    return List

# Main:
List = eval(input("Enter the list in standard list format: "))
print("Sorted List is: ", SelectionSort(List))