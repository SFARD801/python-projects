# convert functions:
def to_binary(x):
    print("Binary =", bin(x))
    ask()


def to_octa(x):
    print("Octal =", oct(x))
    ask()


def to_hex(x):
    print("Hexadecimal =", hex(x))
    ask()


# recursive function:
def ask():
    answer = int(input("Go Again?\n0)No\n1)Yes\n"))
    if answer == 1:
        main()
    elif answer == 0:
        return 0
    else:
        print("ERROR! Please use '1' or '0' as an input.")
        ask()


# main input function:
def main():
    option = int(input("To which base should it be convert? to...\n1)Binary\n2)Octal\n3)Hexadecimal\n"))
    if option == 1:
        to_binary(Input)
    elif option == 2:
        to_octa(Input)
    elif option == 3:
        to_hex(Input)
    else:
        print("ERROR! Please type in the appropriate Number according to the selections below:\n")
        main()


# how to start the program:
Input = int(input("Please provide a number:\t"))
main()

