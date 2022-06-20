#single dimension list

ll = [1, 2, 3, 16, 17]
print(ll)

#two dimensional list
matrix = [
    [1, 2, 4],
    [3, 7, 0],
    [10, 32, 14]

]
#prints the whole matrix
print(matrix)

#print element in 0 indexed
print(matrix[0])

# print element on slot 1 in list index 0
print(matrix[0][1])

# there dimensional list

cc = [
    [
        [1, 2, 4],
        [1, 3, 6],
        [1, 10, 3],
    ],

    [
        [10, 12, 14],
        [11, 13, 16],
        [111, 110, 113],

    ]

]

print(cc) # prints the matrix
print(cc[0][0][1])  # prints element 1 in matrix index 0 list index 0

# matrix of 0 with 5 rows and 7 columns
n = 5
m = 7

mm = []
for _ in range(n):
    ll = []
    for _ in range(m):
        ll.append(0)
    mm.append(ll)

print(f'\n'.join(str(x) for x in mm))

#nested comprehension matrix
print(list([v + 1 for v in row] for row in mm))

#primary diagonal = row index = column index
#secondary diagonal = row index = n - column index - 1 # n count of rows
#below primary diagonal = column index < row index
#above primary diagonal = column index > row index
#below or on primary diagonal = column index <= row index
    






