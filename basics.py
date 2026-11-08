

name = "andrew"
print("len on a str returns nb of chars.",len(name))

users = ["standard_user","problem_user","error_user"]
print("len on a list returns nb of elements inside the list.",len(users))
print(users[0], users[2])

print(users[1])
print("users has", len(users),"users saved")
users.append("locked_out_user") #adds a new user at the end of the list users.


for user in users:
    print(user, end=" ") # overrides the print's default behavior from newline
                         # to space on each print

print(end="\n") #to return the print to its default behavior to \n after every print.
age = 21

if age <= 18:
    print("underage")
elif age <= 22:
    print("teen")
else:
    print("adult")



def function(age):
    year_of_birth = 2026-age
    print("You were born in the year",year_of_birth)

function(age) #function must be declared before i can call it.

def functionBool(age):
    age_bool = age<22
    return(age_bool)

print("Is your age less than 22? =>",functionBool(age)) #returns true


#Dictionaries:
bookings = {"firstname":"user",
            "lastname":"test",
            "age": 25}

print(bookings["firstname"])

for key in bookings:
    print(bookings[key], end=" ")

print(end="\n")


#Exercise:
def is_valid_password(password):
    if ( (8 <= len(password)) and (len(password) <= 16) and (any(char.isdigit() for char in password)) and (any(char.isupper() for char in password)) ):
        return True
    else:
        return False

# print("is password123 valid?",is_valid_password("password123"))
# print("is pass valid?",is_valid_password("pass"))

passwords = ["Passwo1", "Passwor6", "Password1", "Passwordpasswo1", 
             "Passwordpasswor6", "Passwordpassword1", "Passwordpassw", "passwordpass1"]

for password in passwords:
    print(f"is {password} valid?",is_valid_password(password))
