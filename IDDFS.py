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

sn = int(input("source node: "))
lm = int(input("Depth Limit: "))

for depth in range(lm + 1):
    stack = []
    visited = [0 for i in range(n)]
    pr = []
    lvl = [0 for i in range(n)]

    stack.append(sn)
    visited[sn] = 1

    while len(stack) != 0:
        cn = stack.pop(-1)
        pr.append(cn)
        for i in range(n):
            if (am[cn][i] == 1 and visited[i] != 1 and lvl[cn] < depth):
                lvl[i] = lvl[cn] + 1
                stack.append(i)
                visited[i] = 1


    print("Depth:", depth, "Path:", pr)
