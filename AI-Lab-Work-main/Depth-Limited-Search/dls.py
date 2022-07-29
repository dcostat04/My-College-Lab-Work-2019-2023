graph = {
    '0': ['1','2'],
    '1': ['3','4'],
    '2': ['5'],
    '3':[],
    '4':['6'],
    '5':[],
    '6':[],
}

def dls(start,goal,path,level,max_depth):
    print("Current level -->",level)
    path.append(start)
    if(start==goal):
        print("goal success\n")
        return path
    print("goal failure\n")
    if level == max_depth:
        return False

    for child in graph[start]:
        if dls(child,goal,path,level + 1,max_depth):
            return path
        path.pop()
    return False

start='0'
goal= str(input("Enter the Goal Node:"))
path=[]
max_depth=int(input("Enter the Max Depth:"))
res=dls(start,goal,path,0,max_depth)

if (res):
    print("Path to Goal available")
    print("Path:",path)
else:
    print("Path to Goal not available")
