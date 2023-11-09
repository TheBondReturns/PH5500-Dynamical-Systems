#-----------------------------------------------------------------------
# percolationio.py
#-----------------------------------------------------------------------

import sys
import stdarray
import stddraw
import stdrandom
import numpy as np
import time as time
import matplotlib.pyplot as plt


#-----------------------------------------------------------------------

# Return a random n-by-n matrix, each entry True with probability p.

def random(n, p):
    a = stdarray.create2D(n, n, False)
    for i in range(n):
        for j in range(n):
            a[i][j] = stdrandom.bernoulli(p)
    return a

#-----------------------------------------------------------------------

# Draw system a to standard draw. Parameter which indicates whether
# to display the entries corresponding to True or to False.

def draw(a, which):
    n = len(a)
    stddraw.setXscale(-.5, n)
    stddraw.setYscale(-.5, n)
    for i in range(n):
        for j in range(n):
            if a[i][j] == which:
                stddraw.filledSquare(j, n-i-1, .5)

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
                test[j*b0:(j+1)*b0,k*b0:(k+1)*b0]=np.array([[1,1],[1,1]])
            else:
                test[j*b0:(j+1)*b0,k*b0:(k+1)*b0]=np.array([[0,0],[0,0]])
            
          #  array.append(x)
        #renormalized_matrix.append(array)

    return test


#dfs code for checking connectivity

def is_connected(matrix):
     
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


    


#-----------------------------------------------------------------------

# For testing.

def main():
    n = int(sys.argv[1])
   # n2 = int(sys.argv[2])
    p = float(sys.argv[2])
   # array = np.arange(n1,n2,1000)
    p_array = np.arange(0.1,0.9,0.01)
   # for n in array:
    test = random(n,p)
    renorm = np.array(test)
    print(n)
    
    i = 0
    while i<7:
        stddraw.clear()
        renorm = renormalize(renorm,2)
        draw(renorm,True)
        stddraw.show(1000)
        time.sleep(1)
        i+=1

 #   draw(renorm,True)
 #   stddraw.show(5000)
 #   stddraw.clear()

    #draw(test,True)
    #stddraw.show(5000)
    #stddraw.clear()   
    #draw(renorm,True)
    #stddraw.show()









  
if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------

# python percolationio.py 10 0.8
