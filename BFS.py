import collections

def BFS_Traversal(Graph, Root):
    visited = set()                         # We use Set so as to not take in repeated values
    Queue = collections.deque([Root])       # dequeue of Collections library is a double ended Queue

    while Queue:
        vertex = Queue.popleft()            # make the queue enqueue from right and dequeue from left
        visited.add(vertex)                 # Add vertex to Visited set if it is not already present

        for node in Graph[vertex]:
            if node not in visited:
                Queue.append(node)

    return visited


#  Root -> (0)----(1)    (4)   
#           |  \   |    /
#           |   \  |   /             <--- The Graph in the Example
#           |    \ | /
#          (3)    (2)

Graph = {0:[3,1,2], 1:[0,2], 2:[0,1,4], 3:[0], 4:[2]}
Root = 0

print("Breadth-First Search of the Graph is: ", BFS_Traversal(Graph, Root))