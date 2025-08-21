import secrets


def generate_password(length, characters):
    password = []
    for _ in range(length):
        password += secrets.choice(characters)
    for i in range(length-1, 0, -1):
        j = secrets.randbelow(length)
        password[i], password[j] = password[j], password[i]
    password = ''.join(password)
    return password