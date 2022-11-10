"""
An integer partition of n is a weakly decreasing list of positive integers which sum to n.

For example, there are 7 integer partitions of 5:

[5], [4,1], [3,2], [3,1,1], [2,2,1], [2,1,1,1], [1,1,1,1,1].
Write a function which returns the number of integer partitions of n.
The function should be able to find the number of integer partitions of n for n at least as large as 100.
"""

def partitions(n):
    matrix = [[1] * (n + 1)]
    for i in range(1, n + 1):
        matrix.append([0])
        for j in range(1, i + 1):
            if j > i - j:
                num = matrix[i - j][i - j]
            else:
                num = matrix[i - j][j]
                
            matrix[i].append(matrix[i][j - 1] + num)
    return matrix[n][n]
