visited = set()

def DFS(Graph, Root):
    if Root not in visited:
        visited.add(Root)
        print(Root, end=' ')
        for adjacent_node in Graph[Root]:
            DFS(Graph, adjacent_node)

#  Root -> (0)----(1)    (4)   
#           |  \   |    /
#           |   \  |   /             <--- The Graph in the Example
#           |    \ | /
#          (3)    (2)

Graph = {0:[3,1,2], 1:[0,2], 2:[0,1,4], 3:[0], 4:[2]}
Root = 0
print("Depth-First Search Traversal of the Graph is: ", end = '')
DFS(Graph, Root)    