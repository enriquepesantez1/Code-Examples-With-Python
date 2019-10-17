# CMPT 120 - Lab #6
# Enrique Pesantez
# 10-17-2019

# This is the intro for the program
def show_intro():
    print('Wlecome to the Arithmetic Engine!')
    print('=================================\n')
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n")

# This displays the outro of the program
def show_outro():
    print('\nThank you for using the Arithmetic Engine...')
    print('\nPlease come back again soon!')

# Main function of the program
def do_loop():

    while True:
    # Asks for the input of the user
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the Second Number: "))
        cmd = input('What computation do you want to perfrorm? Or type quit to exit: ')
        cmd.lower()
        # Series of if statements that check the user commands
        if cmd == 'add':
            result = num1 + num2
            break
        elif cmd == 'sub':
            result = num1 - num2
            break
        elif cmd == "mult":
            result = num1 * num2
            break
        elif cmd == 'div':
            try:
                result = num1 / num2
            except:
                print("Unable to Divide by zero!")
                continue
        elif cmd == 'quit':
            break
        else:
            print(cmd, "is not a valid command")
            continue
        # Prints the result of the program
        print('The result is:', result, '\n')

# Main function of the program that runs it
def main():
    show_intro()
    do_loop()
    show_outro()

main()
