import string
import random

length = int(input("Enter the length of password: "))
alphabet = string.ascii_letters + string.digits
password = "".join(random.choice(alphabet) for i in range(length))

print(password)
