# [1,2,2]
# [3,1,2]
# [3,3,1]





matrix = []
numbers = int (input("Wie groß ist matrix?:"))
for i in  range (numbers):
    matrix.append ([0]*numbers)

for i in range (numbers):
    for j in range (numbers):
        if i == j:
            matrix [i][j] = 1
        elif i < j:
            matrix [i][j]  = 2
        else:
            matrix [i][j] = 3
for i in matrix:
    print (i)                        
