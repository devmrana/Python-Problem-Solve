# accept a filename from the user and print the extension
# filename = input("Input the Filename: ")
# f_extns = filename.split(".")
# print ("The extension of the file is : " + repr(f_extns[-1]))

file_name = input("Input the Filename: ")
counter = 0
for a in file_name:
    counter += 1 # counter = counter + 1
    if a == ".":
        b = file_name[counter:]
        print(f"The extension of the file is:",b)