class NewNode:
    def __init__(self, data):
        self.value = data
        self.right = None
        self.left = None

def Recursive_Inorder_Traversal(Root):
    if Root:
        Recursive_Inorder_Traversal(Root.left)
        print(Root.value, end=" ")
        Recursive_Inorder_Traversal(Root.right)

RootNode = NewNode(10)
RootNode.left = NewNode(20)
RootNode.right = NewNode(30)
RootNode.left.left = NewNode(40)
RootNode.left.right = NewNode(50)
RootNode.right.left = NewNode(60)

print("Inorder Traversal: ", end='')
Recursive_Inorder_Traversal(RootNode)