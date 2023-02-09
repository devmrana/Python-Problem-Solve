# Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

# Mat size must be N*M. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.
# Sample Designs

#     Size: 7 x 21 
#     ---------.|.---------
#     ------.|..|..|.------
#     ---.|..|..|..|..|.---
#     -------WELCOME-------
#     ---.|..|..|..|..|.---
#     ------.|..|..|.------
#     ---------.|.---------
    
#     Size: 11 x 33
#     ---------------.|.---------------
#     ------------.|..|..|.------------
#     ---------.|..|..|..|..|.---------
#     ------.|..|..|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|..|..|.---
#     -------------WELCOME-------------
#     ---.|..|..|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|..|..|.------
#     ---------.|..|..|..|..|.---------
#     ------------.|..|..|.------------
#     ---------------.|.---------------
# Input Format

# A single line containing the space separated values of  and .

# Constraints

# Output Format

# Output the design pattern.

# Sample Input

# 9 27
# Sample Output

# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------


Row,Colounm = map(int,input().split(' '))

for i in range(1,Row,2):
    print((".|." *i).center(Colounm,"-"))
    
print("Welcome".center(Colounm,"-"))

for i in range(Row-2,-1,-2):
    print((".|." *i).center(Colounm,"-"))
    