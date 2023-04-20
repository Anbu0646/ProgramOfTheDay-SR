'''
The program must accept an integer matrix of size RxC as the input. The program must print the count of submatrices of size 2x2 having the sum as odd. 

Boundary Condition(s): 2 <= R, C <= 50 

Input Format:  The first line contains the values of R and C separated by a space. The next R lines contain C integers separated by space(s). 
Output Format: The first line contains the count of submatrices of size 2x2 having the sum as odd. 

Example Input/Output 1: 

Input:  3 4 
        2 5 1 8
        1 4 7 3 
        6 1 8 5 
        
Output: 3 

Explanation: There are 3 submatrices of size 2x2 having the sum as odd. They are given below. 
             Submatrix 1: 5 1 4 7 Sum = 5 + 1 + 4 + 7 = 17 
             Submatrix 2: 1 8 7 3 Sum = 1 + 8 + 7 + 3 = 19
             Submatrix 3: 7 3 8 5 Sum = 7 + 3 + 8 + 5 = 23 
             
Example Input/Output 2: 

Input:  5 4 
        24 20 13 40
        19 34 28 15 
        16 22 28 13
        29 31 22 36 
        38 22 24 14
        
Output: 6

SOLUTION:
'''

R, C = map(int, input().split())
Mat = [list(map(int, input().split())) for i in range (R)]

count = 0

for i in range(R - 1):
    for j in range(C - 1):
        submat =  Mat[i][j] + Mat[i][j + 1] + Mat[i + 1][j] + Mat[i + 1][j + 1]
        
        if submat % 2 != 0:
            count += 1

print(count)
