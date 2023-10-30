import java.io.Serializable;

public class User implements Serializable {
    private String username;
    private String password;
    private String hint;
    private String firstName;
    private String lastName;

    public User(String username, String password, String hint, String firstName, String lastName) {
        this.username = username;
        this.password = password;
        this.hint = hint;
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public String getHint() {
        return hint;
    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

}
