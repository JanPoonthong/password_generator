import secrets
import string


def generate():
    website = input("What is the website name: ")

    while True:
        try:
            pass_length = int(input("Enter the length of password: "))
            break
        except ValueError:
            print("Input not a number")

    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(pass_length))

    with open("password.txt", "a+") as f:
        print("Writing account info to file")
        f.write(f"Website: {website}\n")
        f.write(f"Password: {password}\n")

    return (website, password)


print(generate())
