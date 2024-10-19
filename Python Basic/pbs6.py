# comma-separated numbers from user and generate a list and a tuple with those numbers

# values = input("Input some comma seprated numbers : ")
# list = values.split(",")
# tuple = tuple(list)
# print('List : ',list)
# print('Tuple : ',tuple)
# ------------------------------------

def input(*args):
    k = []
    for i in args:
        k.append(i)
    m = list(k)
    l = str(m).split(",")
    print(l)
input(1,2,3,4,5,6)

