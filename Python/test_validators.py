
import pytest
from validators import is_valid_password,is_valid_postal

# so pytest auto tests these functions using my test boundary value and expect and actual status code must match.
def test_8_char_valid():
    assert is_valid_password("Passwor6") == True


def test_7_char_invalid():
    assert is_valid_password("Passwo1") == False



# use this if one test can have many inputs like validating a password
@pytest.mark.parametrize("password, expected",[("Passwor6",True),("Passwo1",False)])    
    
def test_password_rules(password,expected):
    assert is_valid_password(password) == expected



# Exercises:
@pytest.mark.parametrize("password, expected",[("Passwo1",False),("Passwor6",True),("Password1",True),
                                               ("Passwordpasswo1",True),("Passwordpasswor6",True),
                                               ("Passwordpassword1",False),("Passwordpassw",False),
                                               ("passwordpass1",False)])#,
                                               #("pass",True)]) #this password should return false but testing error.

def test_password_rules2(password,expected):
    assert is_valid_password(password) == expected


@pytest.mark.parametrize("code, expected",[("12345",True),("1234",False),("12a45",False),
                                               ("123456",False)])


def test_postal_rules(code,expected):
    assert is_valid_postal(code) == expected