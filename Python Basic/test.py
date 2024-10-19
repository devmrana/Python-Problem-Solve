# x = 'hi this is hussein asadi from iran '

# x = x.title()

# print (x)
from numpy import random
def ludo():
    list1 = [1,2,3,4,5,6]
    x = random.choice(list1)
    print(x)
# ludo()
for i in range(1,6):
    print(f'........outside-{i}.......')

    for j in range(1,6):
        print(f'Inside: {j}')

def getPrimeNum(num):
    if num>1:
        for i in range(2,num):
            # print(i)
            if (num%i)==0:
                print (f"\t\t\t{num} It's not a prime number")
                break
        else:
            print(f'\t\t\t {num} is a prime') 
    else:
        print(f"\t\t\t {num} is not a prime number")
    return num
getPrimeNum(790)