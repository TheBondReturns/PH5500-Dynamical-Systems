import sys
import stdarray
import stddraw
import stdrandom
import numpy as np
import time as time

def random(n, p):
    a = stdarray.create2D(n, n, False)
    for i in range(n):
        for j in range(n):
            a[i][j] = int(stdrandom.bernoulli(p))
    return a

def renormalize(test,b0):
    renormalized_matrix = []
    a = [[0,1],[1,1]]
    b = [[1,0],[1,1]]
    c = [[1,1],[0,1]]
    d = [[1,1],[1,0]]
    #e = [[0,0],[1,1]]
    #f = [[1,1],[0,0]]
    g = [[1,0],[1,0]]
    h = [[0,1],[0,1]]
    i = [[1,1],[1,1]]
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    d = np.array(d)
    #e = np.array(e)
    #f = np.array(f)
    g = np.array(g)
    h = np.array(h)
    i = np.array(i)
    for j in range(int(len(test)/b0)):
        array = []
        for k in range(int(len(test)/b0)):
            test = np.array(test)
            selected_rows = test[j*b0:(j+1)*b0]  
            sub_matrix = [row[k*b0:(k+1)*b0] for row in selected_rows]  
            sub_matrix = np.array(sub_matrix)

            # sub_matrix = test[j*b0:(j+1)*b0, k*b0:(k+1)*b0]
            if ((sub_matrix - a) == 0).all() or ((sub_matrix - b) == 0).all() or ((sub_matrix - c) == 0).all() or ((sub_matrix - d) == 0).all() or ((sub_matrix - g) == 0).all() or ((sub_matrix - h) == 0).all() or ((sub_matrix - i) == 0).all():
                x = 1
            else:
                x = 0
            
            array.append(x)
        renormalized_matrix.append(array)

    return renormalized_matrix
    


def percolate(matrix):
     
    ones_prev_row=[]
    for i in range(len(matrix[0])):
        if matrix[0][i]==1:
            ones_prev_row.append(i)
    
    if len(ones_prev_row)==0:
        return False
    
    for rowno in range(1,len(matrix)):

        valid_ones_in_current_row=[]
        for i in ones_prev_row:
            if matrix[rowno][i]==1:
                valid_ones_in_current_row.append(i)
        
        if len(valid_ones_in_current_row)==0:
            return False

        final_curr_ones =[]
        for i in valid_ones_in_current_row:
            temp = i
            if i in final_curr_ones:
                continue
            
            if i!=0:
                while matrix[rowno][i] ==1:
                    final_curr_ones.append(i)
                    i-=1
                    if i<0:
                        break
            
            if temp != len(matrix[0])-1:
                i=temp+1
                while matrix[rowno][i] ==1:
                    final_curr_ones.append(i)
                    i+=1
                    if i == len(matrix[0]):
                        break
                
            ones_prev_row=final_curr_ones

    return True



    


def main():
    n = int(sys.argv[1])
    p = float(sys.argv[2])
    b = int(sys.argv[3])
    test = random(n,p)
    i = 0
    renorm = test
    while i<7:
        renorm = renormalize(renorm,b)
        i+=1
    print(np.matrix(renorm))
    renorm = bool(renorm)
if __name__ == '__main__':
    main()



