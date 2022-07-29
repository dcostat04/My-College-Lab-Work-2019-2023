graph={
    '0':['1','2','3'],
    '1':['4'],
    '2':[],
    '3':['5','6'],
    '4':[],
    '5':[],
    '6':[]
}

visited=[]
queue=[]
source_node='0'

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print(m,end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("The BFS for the Graph is :")
bfs(visited,graph,source_node)
