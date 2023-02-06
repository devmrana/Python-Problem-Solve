fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("Hello  " + lname + " " + fname)
# --------------------------------------
def user(first_name, last_name):
    print("User's Full Name:", last_name.capitalize(), first_name.capitalize(), sep=' ')
fname = input('Please Enter Your First Name: ')
lname = input('Please Enter Your Last Name: ')
user(fname, lname)