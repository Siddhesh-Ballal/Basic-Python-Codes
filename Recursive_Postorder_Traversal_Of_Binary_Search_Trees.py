class NewNode:
    def __init__(self, data):
        self.value = data
        self.right = None
        self.left = None

def Recursive_Postorder_Traversal(Root):
    if Root:
        Recursive_Postorder_Traversal(Root.left)
        Recursive_Postorder_Traversal(Root.right)
        print(Root.value, end=" ")

RootNode = NewNode(10)
RootNode.left = NewNode(20)
RootNode.right = NewNode(30)
RootNode.left.left = NewNode(40)
RootNode.left.right = NewNode(50)
RootNode.right.left = NewNode(60)

print("Postorder Traversal: ", end='')
Recursive_Postorder_Traversal(RootNode)