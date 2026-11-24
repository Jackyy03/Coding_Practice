# # Reverse The Number
# Given an Integer N, write a program to reverse it.
# Input
# The first line contains an integer T, total number of testcases. Then follow T lines, each line contains an integer N.

t=int(input())
for t in range(t):
    a=int(input())
    rev=0
    while a>0:
        ld=a%10
        rev=rev*10+ld
        a=a//10
        
    print(rev)