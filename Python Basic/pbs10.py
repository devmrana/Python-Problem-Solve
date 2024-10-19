# accepts an integer (n) and computes the value of n+nn+nnn

while True:
    def num(n):
        ans = int(n) + int(n+n) + int(n+n+n)
        return ans
    n = input("Enter the number:- ")
    print(num(n))

    # abs(__doc__)
    # func_help = input("Enter a valid Python function name: ")
    # display = help(func_help)
    # print(display)
