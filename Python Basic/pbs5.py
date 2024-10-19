# fname = input("Input your First Name : ")
# lname = input("Input your Last Name : ")
# print ("Hello  " + lname.capitalize() + " " + fname.capitalize())
# --------------------------------------
def user(first_name, last_name):
    if (first_name or last_name) =="":
        print("Write your full name")
    else:
        if len(first_name)>10 or len(last_name)>10:
            print("Name is too long")
        elif len(first_name)<3 or len(last_name)<3:
            print("Name is too short")
        else:
            print("User's Full Name:", last_name.capitalize(), first_name.capitalize(), sep=' ')
            
        
    
fname = input('Please Enter Your First Name: ')
lname = input('Please Enter Your Last Name: ')
user(fname, lname)