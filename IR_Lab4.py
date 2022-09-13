# 2 x 3 matrix 
A = [ [ 2, 5, 7 ],[ 4, 7, 9 ] ]
print(A)

R = int(input("Enter the number of rows:")) 
C = int(input("Enter the number of columns:")) 
  
# Initialize matrix 
matrix = [] 
print("Enter the entries rowwise:") 
  
# For user input 
for i in range(R):          # A for loop for row entries 
    a =[] 
    for j in range(C):      # A for loop for column entries 
         a.append(int(input())) 
    matrix.append(a) 

print(matrix)
# For printing the matrix 
for i in range(R): 
    for j in range(C): 
        print(matrix[i][j], end = " ") 
    print() 

mat = [[int(input()) for x in range (C)] for y in range(R)] 
print(mat)

import numpy as np 
entries = list(map(int, input().split())) 
print(entries) 
matrix = np.array(entries).reshape(R, C) 
print(matrix)
print(matrix[0][0])

x = np.array([[1, 2], [4, 5]]) 
y = np.array([[7, 8], [9, 10]]) 
  
# using add() to add matrices 
print ("The element wise addition of matrix is : ") 
print (np.add(x,y)) 
  
# using subtract() to subtract matrices 
print ("The element wise subtraction of matrix is : ") 
print (np.subtract(x,y)) 
  
# using divide() to divide matrices 
print ("The element wise division of matrix is : ") 
print (np.divide(x,y))

# using multiply() to multiply matrices element wise 
print ("The element wise multiplication of matrix is : ") 
print (np.multiply(x,y)) 
  
# using dot() to multiply matrices 
print ("The product of matrices is : ") 
print (np.dot(x,y)) 
print(x @ y)
print(np.matmul(x,y))
print(2*x)
print(np.multiply(2,x))

# using sqrt() to print the square root of matrix 
print ("The element wise square root is : ") 
print (np.sqrt(x)) 
  
# using sum() to print summation of all elements of matrix 
print ("The summation of all matrix element is : ") 
print (np.sum(y)) 
  
# using sum(axis=0) to print summation of all columns of matrix 
print ("The column wise summation of all matrix  is : ") 
print (np.sum(y,axis=0)) 
  
# using sum(axis=1) to print summation of all rows of matrix 
print ("The row wise summation of all matrix  is : ") 
print (np.sum(y,axis=1)) 

x1 = range(6)
# [0, 1, 2, 3, 4, 5]
print(np.power(x1, 3))
# [  0,   1,   8,  27,  64, 125]

# Raise the bases to different exponents.
x2 = [1.0, 2.0, 3.0, 3.0, 2.0, 1.0]
print(np.power(x1, x2))
# [  0.,   1.,   8.,  27.,  16.,   5.]

# The effect of broadcasting.
x2 = np.array([[1, 2, 3, 3, 2, 1], [1, 2, 3, 3, 2, 1]])
# array([[1, 2, 3, 3, 2, 1],
#        [1, 2, 3, 3, 2, 1]])
print(np.power(x1, x2))
# array([[ 0,  1,  8, 27, 16,  5],
#        [ 0,  1,  8, 27, 16,  5]])  

# using "T" to transpose the matrix 
print ("The transpose of given matrix is : ") 
print (x.T) 

print(x.min())
print(x.max())
x = np.array([[4, 5, 6],
              [8, 1, 10], 
              [7, 12, 5]]) 
print(x[:,2]) # print the 3rd column 
print(x[1,:]) # print the 2nd row
print(x[:,2].min()) # print min value in 3rd column
print(x[1:,1:])
#####################################################

