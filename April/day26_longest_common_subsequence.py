text1 = "cacehce"
text2 = "abcdefchaceh"

def longestCommonSubsequence(text1, text2):
    mat = [[0 for i in range(len(text2) + 1)] for j in range(len(text1) + 1)]

    for i in range(1, len(text1) + 1):
        for j in range(1, len(text2) + 1):
            if text2[j-1] == text1[i-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                mat[i][j] = max(mat[i-1][j], mat[i][j-1])

    return mat[-1][-1]

    """if len(text1) < len(text2):
        shortest_st = text1
        longer_st = text2
    else:
        shortest_st = text2
        longer_st = text1
    
    sequence_dict = {}
    for s in shortest_st:
        if sequence_dict.get(s):
            sequence_dict[s] += 1
        else:
            sequence_dict[s] = 1
    
    indexes = []
    counts = []
    highest_index = 0
    for s in longer_st:
        if sequence_dict.get(s):
            smallest_index = sequence_dict[s][0]
            added = False
            for i in range(len(indexes)):
                if smallest_index > indexes[i]:
                    indexes[i] = smallest_index
                    counts[i] += 1
                    added = True
                if not added:
                    indexes.append(smallest_index)
                    counts.append(1)
    
            if smallest_index < highest_index:
                for i in range(len(sequence_dict[s])):
                    if sequence_dict[s][i] > highest_index:
                        #then add it to values in indexes with """





print(longestCommonSubsequence(text1, text2))