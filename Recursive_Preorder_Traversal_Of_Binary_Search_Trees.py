class NewNode:
    def __init__(self, data):
        self.value = data
        self.right = None
        self.left = None

def Recursive_Preorder_Traversal(Root):
    if Root:
        print(Root.value, end=" ")
        Recursive_Preorder_Traversal(Root.left)
        Recursive_Preorder_Traversal(Root.right)

RootNode = NewNode(10)
RootNode.left = NewNode(20)
RootNode.right = NewNode(30)
RootNode.left.left = NewNode(40)
RootNode.left.right = NewNode(50)
RootNode.right.left = NewNode(60)

print("Preorder Traversal: ", end='')
Recursive_Preorder_Traversal(RootNode)