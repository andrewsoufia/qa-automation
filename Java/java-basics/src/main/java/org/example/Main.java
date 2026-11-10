package org.example;



public class Main {
    public static void main(String[] args) {

        String[] passwords = {"Passwo1", "Passwor6", "Password1",
                "Passwordpasswo1", "Passwordpasswor6",
                "Passwordpassword1", "Passwordpassw",
                "passwordpass1"};

        String[] codes = {"12345", "12a34", "45A67", "1234", "123456", " 1234", "  ", "       "};

        for (String pass : passwords) {
            System.out.println(pass + " = " + isValidPassword(pass));
        }

        for (String code : codes) {
            if(code.isBlank()){
                System.out.println("code cannot be empty");
            }else{
            System.out.println(code + " = " + isValidPostal(code));
            }
        }
    }


    public static boolean isValidPassword(String password){

        boolean hasUppercase = false;
        boolean hasDigit = false;

        if ( (8 <= password.length()) && (password.length() <= 16) ){

            for(char c: password.toCharArray()){
                if(Character.isUpperCase(c)){
                    hasUppercase =  true;
                }
                if(Character.isDigit(c)){
                    hasDigit =  true;
                }
            }
            if (hasDigit && hasUppercase){
                return true;
            }else{
                return false;
            }
        }
        else{
            return false;
        }
    }


    public static boolean isValidPostal(String code){

        int digitPostalCount = 0;

        if ( code.length() == 5 ){

            for(char c: code.toCharArray()){
                if(Character.isDigit(c)){
                    digitPostalCount =  digitPostalCount + 1;
                }
            }
            if (digitPostalCount == 5){
                return true;
            }else{
                return false;
            }
        }
        else{
            return false;
        }
    }
}