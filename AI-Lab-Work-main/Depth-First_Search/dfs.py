graph={
    '0':['1','2','3'],
    '1':['4'],
    '2':[],
    '3':['5','6'],
    '4':[],
    '5':[],
    '6':[]
}

visited=set()
source_node='0'

def dfs(visited,graph,node):
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

print("The DFS for the following graph is: ")
dfs(visited,graph,source_node)
