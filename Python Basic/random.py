from numpy import random
def ludo():
    list1 = [1,2,3,4,5,6]
    for i in range(1,11):
        x = random.choice(list1)
        print(f'Ramdom Value-{i} > {x}')
ludo()