###python program for crisp relation, the program is to generate the composition operation for crisp relation. 
import numpy as np
from colorama import Fore

### This function takes the user input with same number of elements in set 1 and set2####
def UserInput():
  listX =[]
  listY=[]
  print("Enter number of elements X: ")
  nX=int(input())
  print("Enter number of elements Y: ")
  nY = int(input())
  print(Fore.RED + "Enter values for set X: ")
  for i in range(nX):
    x= int(input())
    listX.append(x)
  print("Enter values for set Y: ")
  for j in range(nY):
    y= int(input())
    listY.append(y)
  print("X = {",listX,"}")
  print("Y = {",listY,"}")
  CartesianProduct(listX,listY) ## passing the listX and listY to Cartesianproduct function
  crisprelationRS(listX,listY)## passing the listX and listY to crisprelationRS function
  RSMatrix(listX,listY)## passing the listX and listY to RSMatrix function

###This function creates cartesian product of two sets
def CartesianProduct(listX,listY):
  print()
  print(Fore.BLUE+"cartesian product of X and Y")
  print("{",end="")
  for k in listX:
    for m in listY:
      print((k,m),end=",")
  print("}")

#### This function creates a crisp relation for R and S 
def crisprelationRS(listX,listY):
  print()
  print(Fore.GREEN+"R relation: ")
  print("{",end="")
  for k in listX:
    for m in listY:
      if (k+2==m): ### Here you can change the conditions
        print((k,m),end=",")
  print("}")
  print()
  print("S relation: ")
  print("{",end="")
  for k in listX:
    for m in listY:
      if (k<m):
        print((k,m),end=",")
  print("}")
### This function is used to generate R and S matrices
def RSMatrix(listX,listY):
  print()
  print(Fore.MAGENTA)
  print("Enter rows and columns matched values for R: ")
  m = []
  for n in range(len(listX)):
    matrix=[]
    for o in range(len(listX)):
      print("Enter the value for: ",(listX[n],listY[o]))
      matrix.append(int(input()))
    m.append(matrix)
  R_matrix = np.array(m)
  print("R matrix is : \n",R_matrix)
  print()
  print(Fore.LIGHTGREEN_EX)
  print("Enter rows and columns matched values for S: ")
  m1 = []
  for n in range(len(listX)):
    matrix1=[]
    for o in range(len(listY)):
      print("Enter the value for: ",(listX[n],listY[o]))
      matrix1.append(int(input()))
    m1.append(matrix1)
  S_matrix = np.array(m)
  print("S matrix is : \n",S_matrix)
  MinOperation(R_matrix,S_matrix)## passing the R_matrix and S_matrix to MinOperation function

###This function is used to find the minimum operation  in composition operation  
def MinOperation(R_matrix,S_matrix):
  min_list=[]
  # iterate through rows of R_matrix
  for i in range(len(R_matrix)):
    for j in range(len(S_matrix[0])): #column length to compare the elements number of times
       # iterate through rows of S_matrix
       for k in range(len(S_matrix)):
          min_list.append(min(R_matrix[i][k] , S_matrix[k][j]))
  A=np.array(min_list).reshape(len(R_matrix)*len(R_matrix),len(S_matrix))
  print()
  print(Fore.LIGHTRED_EX+"Minimum operation (Ros): ")
  print(A)
  MaxOperation(A,R_matrix,S_matrix) ## passing the A list,R_matrix and S_matrix to MaxOperation function
 
###This function is used to find the maximum operation which is the next step in composition relation   
def MaxOperation(A,R_matrix,S_matrix):
  print()
  print("composition operation RoS is:")
  com_list=[]
  for i in range(len(A)):
    max_A=max(A[i])
    com_list.append(max_A)
  B=np.array(com_list).reshape(len(R_matrix),len(S_matrix))
  print(B)

UserInput() ### calling the userInput function
