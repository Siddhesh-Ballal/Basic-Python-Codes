Queue = []
Size = 3

def Enqueue(val):
    if len(Queue) < Size:
        Queue.append(val)
    else:
        print("Queue Overflow")

def Dequeue():
    if len(Queue) == 0:
        print("Queue Undeflow")
    else:
        Queue.remove(Queue[0])

def Display():
    print(Queue)

def Peek():
    print("Front = ", Queue[-1])
    print("Rear = ", Queue[0])

Display()
Enqueue(10)
Display()
Enqueue(20)
Display()
Enqueue(30)
Display()
Enqueue(40)

Dequeue()
Display()
Dequeue()
Display()
Dequeue()
Display()

Dequeue()