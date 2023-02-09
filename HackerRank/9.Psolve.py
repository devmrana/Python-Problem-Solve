if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    new_arr = [x for x in arr]
    a = max(new_arr)
    print(f'Old max : {a}')
    count = 0
    for i in new_arr:
        if i == a:
            count +=1
    for j in range(count):
        new_arr.remove(a)
    newMax = max(new_arr)
    print(f'New max: {newMax}')