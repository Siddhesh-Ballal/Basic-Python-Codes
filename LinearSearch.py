def LinearSearch(List, Element):
    for index in range(len(List)):
        if List[index] == Element:
            print(Element, " found at index: ", index)
            break
    else:
        print(Element, " not found in the list")

# main:
List = eval(input("Enter the list in standard list format: "))
Element = int(input("Enter the element: "))

LinearSearch(List, Element)