import sys

def main():
    input = get_user_input()

    if input == 5:
        sys.exit("Program exited")


def greetings():
    print("\nWelcome to Cryptcli 🔐\n")
    print(
"""What would you like to do? 
1. Encrypt a message
2. Decrypt a message
3. Load from file
4. Save to file
5. Exit
""")
    
    
def get_user_input():
    while True:
        try:
            greetings()
            user_input = int(input("> ").strip())
            
            if user_input < 0 or user_input > 5:
                raise ValueError
            else:
                return user_input
        except ValueError:
            continue


def encrypt():
    pass


if __name__ == "__main__":
    main()