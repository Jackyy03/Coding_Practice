# if else 

# Input Format
# The first line will contain 
# T
# T - the number of test cases. Then the test cases follow.
# The first and only line of each test case contains one integer 
# X
# X - the time when Janmansh starts doing the assignments.
# Output Format
# For each test case, output Yes if he can complete the assignments on time. Otherwise, output No.
# You may print each character of Yes and No in uppercase or lowercase (for example, yes, yEs, YES will be considered identical).

# Constraints
# 1
# ≤
# T
# ≤
# 10
# 1≤T≤10
# 1
# ≤
# X
# ≤
# 9
# 1≤X≤9
# Sample 1:
# Input
# Output
# 2
# 7
# 9
# Yes
# No

t = int(input())
for i in range(t):
    a = int(input())
    if a > 7:
        print("No")
    else:
        print("Yes")
        
        

