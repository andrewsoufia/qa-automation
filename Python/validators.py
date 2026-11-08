

#the code under test.
def is_valid_password(password):
    return (8 <= len(password) <= 16
            and any(c.isdigit() for c in password)
            and any(c.isupper() for c in password))


def is_valid_postal(code):
    return ( len(code)==5 and all(char.isdigit() for char in code) )