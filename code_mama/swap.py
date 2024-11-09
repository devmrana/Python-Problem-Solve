num1,num2 = map(int,input().split())
print(f"Before swapping: num1 = {num1}, num2 = {num2}")
temp = num1
num1 = num2
num1 , num2 = num2, num1
num2 = temp
print(f"After swapping: num1 = {num1}, num2 = {num2}")