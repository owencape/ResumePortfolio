public class PasswordChecker {

    public static boolean isPasswordValid(String password) {
        String regex = "^(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&+=])(?=\\S+$).{8,}$";
        return password.matches(regex);
    }
}
