def countSquares(matrix) -> int:
    tot = 0
    for j in range(len(matrix)):
        for i in range(len(matrix[0])):
            if matrix[j][i] == 0: continue

            if i > 0 and j > 0:
                matrix[j][i] = 1 + min(matrix[j-1][i], matrix[j][i-1], matrix[j-1][i-1])
                tot += matrix[j][i]
            else:
                tot += 1

    return tot

# For testing
m = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
n = [[0,1,1,1,1],[1,1,1,1,1],[0,1,1,1,1],[0,1,1,1,1],[1,0,1,1,1]]
p = [[0,1,1,1]]
q = [[0],[1],[1],[1]]
r = [[1]]
s = [[0]]
t = [[1,1,1,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1],[1,1,1,1,1]]
u = [[1,0,1],[1,1,0],[1,1,0]]

for i in [m,n,p,q,r,s,t,u]:
    print(countSquares(i))