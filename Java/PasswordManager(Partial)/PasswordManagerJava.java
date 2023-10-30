import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

// stack overflow used to help us understand how to use and implement Buffered Reader also taught us try and catch 

public class LoginSystem {
    private static final String FILENAME = "users.txt";
    private static int loginAttempts = 0;

    private static ArrayList<User> loadUsers() {
        ArrayList<User> users = new ArrayList<>();
        try (BufferedReader br = new BufferedReader(new FileReader(FILENAME))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] parts = line.split(":");
                String username = parts[0];
                String password = parts[1];
                String hint = parts[2];
                String firstName = parts[3];
                String lastName = parts[4];
                users.add(new User(username, password, hint, firstName, lastName));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return users;
    }

    private static void saveUser(User user) {
        try (BufferedWriter bw = new BufferedWriter(new FileWriter(FILENAME, true))) {
            bw.write(user.getUsername() + ":" + user.getPassword() + ":" + user.getHint() + ":"
                    + user.getFirstName() + ":" + user.getLastName());
            bw.newLine();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static boolean loginUser(String username, String password) {
        ArrayList<User> users = loadUsers();
        for (User user : users) {
            if (user.getUsername().equals(username) && user.getPassword().equals(password)) {
                System.out.println("Welcome, " + username + "!");
                return true;
            }
        }
        System.out.println("Invalid username or password.");
        loginAttempts++;
        if (loginAttempts >= 3) {
            System.out.println("Too many incorrect login attempts. Program shutting down.");
            System.exit(0);
        }
        return false;
    }

   private static void recoverPassword(String username, String firstName, String lastName) {
    ArrayList<User> users = loadUsers();
    for (User user : users) {
        if (user.getUsername().equals(username) && user.getFirstName().equals(firstName) && user.getLastName().equals(lastName)) {
            System.out.println("Your hint: " + user.getHint());
            return;
        }
    }
    System.out.println("User not found or details do not match.");
}


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            System.out.println("\n1. Register");
            System.out.println("2. Login");
            System.out.println("3. Recover Password");
            System.out.println("4. Quit");
            System.out.print("Select an option: ");

            int choice = scanner.nextInt();
            scanner.nextLine();  

            //was looking for an alternative for long conditionals and found switch and case code is perfect for this project

            switch (choice) {
                case 1:
                    
                    System.out.print("Enter your first name: ");
                    String regFirstName = scanner.nextLine();

                    System.out.print("Enter your last name: ");
                    String regLastName = scanner.nextLine();

                    System.out.print("Enter your username: ");
                    String regUsername = scanner.nextLine();

                    System.out.print("Password Requirements: 1 capital letter, 1 number, 1 Symbol: (@#$%^&+=), Atleast 8 letters long\nEnter your password: ");
                    String regPassword = scanner.nextLine();
                    if (PasswordChecker.isPasswordValid(regPassword)) {
                        System.out.print("Enter a hint for your password: ");
                        String regHint = scanner.nextLine();
                        User newUser = new User(regUsername, regPassword, regHint, regFirstName, regLastName);
                        saveUser(newUser);
                        System.out.println("User registered successfully.");
                    } else {
                        System.out.println("Password does not meet requirements.");
                    }

                    break;

                case 2:
                    System.out.print("Enter your username: ");
                    String loginUsername = scanner.nextLine();
                    System.out.print("Enter your password: ");
                    String loginPassword = scanner.nextLine();
                    if (loginUser(loginUsername, loginPassword)) {
                        loginAttempts = 0; 
                    }
                    break;

                case 3:
                
                    System.out.print("Enter your username: ");
                    String recoverUsername = scanner.nextLine();
                    
                    System.out.print("Enter your first name: ");
                    String recoverFirstName = scanner.nextLine();

                    System.out.print("Enter your last name: ");
                    String recoverLastName = scanner.nextLine();
                    
                    recoverPassword(recoverUsername, recoverFirstName, recoverLastName);
                    break;

                case 4:
                    scanner.close();
                    System.exit(0);

                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }
    }
}
