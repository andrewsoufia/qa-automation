package org.example;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.ValueSource;
import static org.junit.jupiter.api.Assertions.*;


class MainTest {

    @Test void testOneInvalidPassword(){

        assertEquals(false,Main.isValidPassword("password"));
    }

    @ParameterizedTest
    @ValueSource(strings = {"Passwo1", "Passwordpassword1",
            "Passwordpassw", "passwordpass1"})
    void testAllInvalidPasswords(String password){

        assertFalse(Main.isValidPassword(password));
    }

    @ParameterizedTest
    @ValueSource(strings = {"Passwor6", "Password1",
            "Passwordpasswo1", "Passwordpasswor6"})
    void validPasswordsPass(String password){
        assertEquals(true,Main.isValidPassword(password));
    }

    @Test
    void validPostalPasses () {
        assertEquals(true, Main.isValidPostal("12345"));
    }

    @ParameterizedTest
    @ValueSource(strings = {"12a34", "1234", "123456", " 1234", ""})
    void invalidPostalsFail (String code){
        assertEquals(false,Main.isValidPostal(code));
    }
}
