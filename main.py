import sys
from encrypt import encrypt
from decrypt import decrypt

def main():
    input = get_user_input()

    if input == 3:
        sys.exit("Program exited")
    elif input == 1:
        print(encrypt())
    elif input == 2:
        print(decrypt())


def greetings():
    print("\nWelcome to Cryptcli 🔐\n")
    print(
"""What would you like to do? 
1. Encrypt a message
2. Decrypt a message
3. Exit
""")
    

def get_user_input():
 
    try:
        greetings()
        user_input = int(input("> ").strip())
        
        if user_input < 0 or user_input > 5:
            raise ValueError
        else:
            return user_input
    except ValueError:
        sys.exit("\nPlease select an option from the menu\n")
    except KeyboardInterrupt:
        sys.exit("\nProgram interupted with Keyboard\n")



if __name__ == "__main__":
    main()