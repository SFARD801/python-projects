#converter functions:
def toBinary(x):
        print(bin(x))
        ask()
def toOcta(x):
        print(oct(x))
        ask()
def toHex(x):
        print(hex(x))
        ask()
#recursive function:
def ask():
    answer=input("again? [Y/N]")
    if answer=="y":
        main()
    elif answer=="n":
        return 0
    else:
        print("ERROR! Please do Enter 'y' or 'n' as an input.")
        ask()
#main input funciton:
def main():
    Input=int(input("Please enter a number:"))
    option=input("to Binary? to Octa? or to Hexa?")
    if option=="binary":
        toBinary(Input)
    elif option=="octa":
        toOcta(Input)
    elif option=="hexa":
        toHex(Input)
    else:
        print("ERROR! Please type in binary , octa or hexa...")
        main()
#how to start the program:
main()
