import secrets
import string

# Random password
def random_password():
    # Define the length of the password
    password_length = 8  # You can adjust this to your desired length

    # Define characters to use for generating the password
    password_characters = string.ascii_letters + string.digits # + string.punctuation

    # Generate a random password
    random_password = ''.join(secrets.choice(password_characters) for i in range(password_length))

    print("Random Password:", random_password)
    return random_password

random_password()