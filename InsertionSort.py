# List is divided into Sorted and Unsorted from the Get go

#               Sorted | Unsorted
#                      ^ 
#                      partition

# When new element from unsorted part is added to Sorted (By moving the partition leftways) 
# The new element is compared with the respective elements of Sorted List to match in correct Position)  

def InsertionSort(List):
    for i in range(1, len(List)):
        j = i
        while List[j] < List[j-1] and j > 0:
            List[j-1], List[j] = List[j], List[j-1]
            j -= 1
    return List

# Main:
List = eval(input("Enter the list in standard list format: "))
print("Sorted List = ", InsertionSort(List))