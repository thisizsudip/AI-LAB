n = int(input("Enter the number of vertex: "))
m = int(input("Enter the number of edge: "))
am = [[-1 for i in range(n)] for j in range(n)]

print("Enter the edges (source destination):")
for i in range(m):
    x = input()
    s, d = int(x.split()[0]), int(x.split()[1])
    am[s][d] = 1
    #am[d][s] = 1

print("Adjacency Matrix:")

for row in am:
    print(row)  

stack = []
visited = [0 for i in range(n)]
print(visited)

sn = int(input("source node: "))

stack.append(sn)
pr = []
visited[sn] = 1

while len(stack) != 0:
    cn = stack.pop(-1)
    pr.append(cn)
    for i in range(n):
        if am[cn][i] == 1 and visited[i] != 1:
            stack.append(i)
            visited[i] = 1

print(pr)            
