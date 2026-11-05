row = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))
mtx = [[-1 for i in range(row)] for j in range(row)]
mtx[0][2] = 1
mtx[1][1] = 1
mtx[2][3] = 1
mtx[3][0] = 1
sr = int(input("Enter the source row: "))
sc = int(input("Enter the source col: "))
gr = int(input("Enter goal row: "))
gc = int(input("Enter goal col: "))

print("Adjacency Matrix:")

for row in mtx:
    print(row)





