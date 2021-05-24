#python program for fuzzy relation with different matrix dimensions
import numpy as np
# This function is used take number of rows and columns and generate two matrices with different dimensions
def FuzzyOperation():
  print("Enter number of rows for D")
  rows=int(input())
  print("Enter number of columns D")
  columns =int(input())
  import numpy as np
  m = []
  for n in range(rows):
    matrix1=[]
    for o in range(columns):
      matrix1.append(float(input()))
    m.append(matrix1)
  D = np.array(m) # generating D matrix
  print("D matrix is : \n",D)
  print()
  print("Enter number of rows G")
  rows1=int(input())
  print("Enter number of columns G")
  columns1 =int(input())
  m2 = []
  for n in range(rows1):
    matrix2=[]
    for o in range(columns1):
      matrix2.append(float(input()))
    m2.append(matrix2)
  G = np.array(m2) # generating G matrix
  print("G matrix is : \n",G)
  MinOperation(D,G) # passing D and G matrices to MinOperation function

#This function is used to find minimum values between D and G matrices by comparing each column in D matrix with row in G matrix
def MinOperation(D,G):
  print()
  min_list=[]
  # iterate through rows of R_matrix
  for i in range(len(D)):
   for j in range(len(G[0])): #column length to compare the elements number of times
       # iterate through rows of S_matrix
       for k in range(len(G)):
          min_list.append(min(D[i][k] , G[k][j]))
  A=np.array(min_list).reshape(len(D)*len(G[0]),len(G))
  print("mininimum operation: \n",A)
  MaxOperation(A,D,G) # passing the minimum values generated and D, G matrices to MaxOperation

# This function is used to find the maximum values from the resultant MinOperation function 
def MaxOperation(A,D,G):
  print()
  com_list=[]
  for i in range(len(A)):
    max_A=max(A[i])
    com_list.append(max_A)
  B=np.array(com_list).reshape(len(D),len(G[0]))
  print("Composition operation: \n",B) # printing the resulant composition operation

FuzzyOperation() # calling the fuzzy operation
