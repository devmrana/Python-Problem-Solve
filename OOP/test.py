d = {'k1': 1, 'k2': 2, 'k3': 3}
for key, value in d.items():
    print(key, '>>>', value)

for item in d.items():
    print(item)


print('-------------------------------------')

import json
data = {
    'name':'Masud',
    'age':30,
    'address':{
        'post':1200,
        'district':'Dhaka'
    }
    
}
d = json.dumps(data) # Python string to convert json string
print(f'Json format >> {d}')

e = json.loads(d) # Json format to convert python string
print(f'Python string format >> {e}')