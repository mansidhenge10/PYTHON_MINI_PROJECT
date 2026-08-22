import random
import string

length = int(input("Password length: "))

chars = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

password = "".join(
    random.choice(chars)
    for _ in range(length)
)

print("\nGenerated password:")
print(password)