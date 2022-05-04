Stack=[]
size = 3

def Push(Val):
    if len(Stack) < size:
        Stack.append(Val)
    else:
        print("Overflow Error")

def Pop():
    if len(Stack) == 0:
        print("Underflow Error")
    else:
        print(Stack.pop())

def Peek():
    if len(Stack) == 0:
        print("Stack is empty")
    else:
        print(Stack[-1])

def Display():
    print(Stack)

Display()
Push(10)
Display()
Push(20)
Display()
Push(30)
Display()

Push(40)

Pop()
Display()
Pop()
Display()
Pop()
Display()

Pop()