#Name: Sudip Paul
#ID: 05624205101061
#Name: MD. Mushfiqur Rahman Arafath
#ID: 05624205101041


row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
mtx = [[-1 for i in range(col)] for j in range(row)]
mtx[0][2] = 1
mtx[1][1] = 1
mtx[2][3] = 1
mtx[3][0] = 1
sr = int(input("Enter the source row: "))
sc = int(input("Enter the source col: "))
gr = int(input("Enter goal row: "))
gc = int(input("Enter goal col: "))

print("Adjacency Matrix:")

for r in mtx:
    print(r)
    
visited = [[False for i in range(col)] for j in range(row)]    

queue = []
parent = {}
queue.append((sr, sc))
visited[sr][sc] = True
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]




