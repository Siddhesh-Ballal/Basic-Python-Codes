# DIVIDE AND CONQUER 
# Divide The Array into two parts
# Keep dividing likewise till we get singular elements 
# Now group the sorted lists by comparing first element of both lists 
# and accepting the lesser one in group
# do it till one group runs out of elements
# Then put the remaining elements of second group in order, as they ar already sorted 
# Keep grouping these till you get sorted array

def MergeSort(List):
    if len(List) > 1:
        LeftHalf = List[:len(List//2)]
        RightHalf = List[len(List)//2:]
        SortedList = list()
        
        # Calling Recursive Merge Sort to divide List in sorted lists of 1 elements

        MergeSort(LeftHalf)
        MergeSort(RightHalf)

        # Now Merging the Sorted Lists by Comparing first elements of each Sub-List

        i=0     # Left Sub-List Index
        j=0     # Right Sub-List Index
        k=0     # Merged List Index

        while i < len(LeftHalf) and j < len(RightHalf):
            if LeftHalf[i] < RightHalf[j]:
                SortedList[k] =  LeftHalf[i]
                i+=1
            else:
                SortedList[k] = RightHalf[j]
                j+=1
            k+=1
            
        while i < len(LeftHalf):
            SortedList[k] = LeftHalf[i]
            i+=1
            k+=1
        
        while j < len(RightHalf):
            SortedList[k] = RightHalf[j]
            j+=1
            k+=1 
    
    return SortedList
    
# Main
List = [9,4,3,6,1,2,5,8,7]
SortedList = MergeSort(List)
print("Sorted List: ", SortedList)