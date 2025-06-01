MIN_LENGTH = 8  # You can change this number

def main():
    password = input("Enter your password: ")
    while len(password) < MIN_LENGTH:
        print(f"Password too short! Must be at least {MIN_LENGTH} characters.")
        password = input("Enter your password: ")

    print("*" * len(password))  # Prints asterisks as long as the password

main()