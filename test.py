try:
    list = 5*[0]+5*[10]
    print(list)
    x = list[90] 
    print(x)
    print('Done!') 
except IndexError: 
   print('Index out of Bond! ') 
else: 
   print('Nothing is wrong!') 
finally: 
   print('Finally block!') 