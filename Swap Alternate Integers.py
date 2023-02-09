'''
The program must accept N integers as the input. The program must swap the first and third integer then the program must swap fourth and sixth integer and so on. 
Finally, the program must print those N integers as the output. 

Note: N is always divisible by 3. 

Boundary Condition(s): 3 <= N <= 999

Input Format:  The first line contains the integer N. The second line contains N integers separated by space.
Output Format: The first line contains N integers separated by space. 

Example Input/Output 1: 

Input:  6 
        1 2 3 4 5 6 
Output: 3 2 1 6 5 4 

Explanation:  The first integer is 1 and the third integer is 3 which are swapped to get 3 2 1. 
The fourth integer is 4 and the sixth integer is 6 which are swapped to get 6 5 4. 

Example Input/Output 2: 

Input:  9 
        4 7 87 9 6 12 44 5 7 
Output: 87 7 4 12 6 9 7 5 44

SOLUTION:
'''
#Michael
n=int(input())
l=list(map(int, input().split()))
for i in range(0, len(l), 3):
    l[i], l[i + 2] = l[i + 2], l[i]
print(*l)
