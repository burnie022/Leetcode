def intervalIntersection(A, B):
    i, j = 0, 0
    result = []
    while i < len(A) and j < len(B):
        if max(B[j][0], A[i][0]) <= min(B[j][1], A[i][1]):
            result.append([max(B[j][0], A[i][0]), min(B[j][1], A[i][1])])

        if B[j][1] > A[i][1]:
            i += 1
        else:
            j += 1
    return result


A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]

tests = {[[0,2],[5,10],[13,23],[24,25]]: [[1,5],[8,12],[15,24],[25,26]]
         }

print(intervalIntersection(A, B))
