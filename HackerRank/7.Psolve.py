# Enter your code here. Read input from STDIN. Print output to STDOUT
Row,Colounm = map(int,input().split(' '))

for i in range(1,Row,2):
    print((".|." *i).center(Colounm,"-"))
    
print("Welcome".center(Colounm,"-"))

for i in range(Row-2,-1,-2):
    print((".|." *i).center(Colounm,"-"))
    