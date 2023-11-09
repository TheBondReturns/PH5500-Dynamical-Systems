import numpy as np
    
def is_connected(matrix):

    ones = []
    for i in range(len(matrix)):
        if matrix[0,i]==1:
            ones.append(i)
            current_pt = [0,i]
        else:
            return False
        
    for j in ones:
        current_pt = [0,ones[-1]]
        x = current_pt[0]
        y = current_pt[1]

    #check all 4 sides

        if x==len(matrix)-1:
            print('a')
            return True
        
        elif x<len(matrix)-1 and y<len(matrix[0])-1:
            print('c')
            if matrix[x+1][y]==1: 
                matrix[x][y]==0
                current_pt_new = [x+1,y] #move down if 1
                return is_connected(matrix,current_pt_new)

            elif matrix[x-1][y]==1: 
                current_pt_new = [x-1,y]
                return is_connected(matrix,current_pt_new)
            
            elif matrix[x][y+1]==1: 
                current_pt_new = [x,y+1]
                return is_connected(matrix,current_pt_new)
            
            elif matrix[x][y-1]==1: 
                current_pt_new = [x,y-1]
                return is_connected(matrix,current_pt_new)

            else: 
                return False
            
        elif y==len(matrix[0]) - 1 and x<len(matrix) - 1:

            if matrix[x][y]!=1:
                print('b')

                return False
            

# Example usage:
matrix = [
    [1, 0, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 1]
]

print(np.matrix(matrix))
current_pt = [0,0]

print(is_connected(matrix,current_pt))

if is_connected(matrix,current_pt):
    print("There is a vertically spanning cluster.")
else:
    print("There is no vertically spanning cluster.")