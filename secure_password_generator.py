from secrets import choice
import string

# Generate a secure password based on user-defined criteria
def choices(alphabet: str, length: int) -> str:
    return "".join(choice(alphabet) for _ in range(length))


# Generate a secure password based on user-defined criteria with unique characters
def sample(alphabet: str, length: int) -> str:
    line = ""
    for _ in range(length):
        line += choice(alphabet)
        alphabet = alphabet.replace(line[-1], "", 1)
    return line


# Ask user for password criteria
def ask_password_criteria(messege: str) -> int:
    while True:
        user_input = input(messege)
        if user_input in ("1", "0"):
            return int(user_input)
        else:
            print("Incorrect input, please enter 1 (YES) or 0 (NO).")


# Function to generate password
def password_generator(len: int, alphabet: str , uniq: int) -> str:
    if uniq:
        return sample(alphabet, len)
    else:
        return choices(alphabet, len)


# Menu
def main() -> None:
    print("""/
                        Welcome to the cryptographically secure password generator. 
        All characters are enabled by default, but you can disable individual characters in the settings.
                    Standart settings: length - 10, characters - all, repetition - allowed.
        """)
    # Default settings
    lenght = 10
    alphabet = string.digits + string.ascii_lowercase + string.ascii_uppercase + string.punctuation
    uniq = 0

    while True:
        dialog = input("""
                    Main menu:
                    1 - Generate a password
                    2 - Settings
                    3 - Exit
                    """)
    
        if dialog == "1":
            for _ in range(int(input("How many passwords do you want to generate? "))):
                print(password_generator(lenght, alphabet, uniq))
        elif dialog == "2":
            lenght, alphabet, uniq = settings()
        elif dialog == "3":
            print("\nSee you later!\n")
            break
        else:
            print("Incorrect input, please try again.")


# Settings menu
def settings() -> tuple[int, str, int]:
    while True:
        length = input("Password length: ")
        if length.isdigit() and int(length) > 0:
            length = int(length)
            break
        else:
            print("Incorrect input, please enter a positive integer.")
    
    while True:
        alphabet = string.digits * ask_password_criteria("Whether to include digits YES(1)/NO(0): ") + \
        string.ascii_lowercase * ask_password_criteria("Whether to include lowercase letters YES(1)/NO(0): ") + \
        string.ascii_uppercase * ask_password_criteria("Whether to include uppercase letters YES(1)/NO(0): ") + \
        string.punctuation * ask_password_criteria("Whether to include punctuation YES(1)/NO(0): ")
        uniq = ask_password_criteria('Do you want the characters in your password to be unique? YES(1)/NO(0): ')
        
        if alphabet == '':
            print("Incorrect input, at least one character type must be selected. Please adjust your settings.")
        elif len(alphabet) < length and uniq == 1:
            print("Incorrect input, the length of the password cannot be greater than the number of available characters. Please adjust your settings.")
        else:
            break

    return length, alphabet, uniq


main()