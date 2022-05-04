def BinarySearch(List, Element, Lower, Upper):
    Mid = (Lower + Upper) // 2
    while(Lower < Upper):
        if List[Mid] == Element:
            return Mid
        elif Element > List[Mid]:
            BinarySearch(List, Element, Mid+1, Upper)
        else:
            BinarySearch(List, Element, Lower, Mid-1)
    return -1
        

# main:
List = [9,8,7,6,3,1,5,4,2]
Element = 4

res = BinarySearch(List, Element, 0, len(List)-1)

if res != -1:
    print(Element , " found at : ", res)
else:
    print(Element, " Not found")