# CMPT 120 - Lab #6
# Enrique Pesantez
# 10-17-2019

def show_intro():
    print('Wlecome to the Arithmetic Engine!')
    print('=================================\n')
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

def show_outro():
    print('\nThank you for using the Arithmetic Engine...')
    print('\nPlease come back again soon!')

def do_loop():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the Second Number: "))
    cmd = input('What computation do you want to perfrorm?: ')
    cmd.lower()
    if cmd == 'add':
        result = num1 + num2
    elif cmd == 'sub':
        result = num1 - num2
    elif cmd == "mult":
        result = num1 * num2
    elif cmd == 'div':
        result = num1 / num2
    elif cmd == 'quit':
        return
    else:
        print(cmd, "is not a valid command")
        return

    print('The result is:', result, '\n')

def main():
    show_intro()
    do_loop()
    show_outro()

main()