


# 1) Predict first, then run. Write down what you think each line prints, then run it and compare:
print("Hello".isupper()) #false must all be Uppercased
print(any(c.isupper() for c in "Hello")) #true
print(all(c.isalpha() for c in "Hello1")) #false
print(any(c.isspace() for c in "my password")) #true


def is_valid_postal(code):
    if ( len(code)==5 and all(char.isdigit() for char in code) ):
        return True
    else:
        return False

codes = ["12345", "1234", "12a45", "123456"]

for code in codes:
    print(f"{code} is valid?",is_valid_postal(code))


def has_lowercase(password):
    if ( any(char.islower() for char in password) ):
        return True
    else:
        return False

passwords = ["PASSWORD1", "Password1"]

for password in passwords:
    print(f"{password} has at least 1 lowercase?",has_lowercase(password))