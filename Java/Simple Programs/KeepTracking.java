import java.util.Scanner;

public class KeepingTrack {
    public static void main(String[] args) {

        Scanner ui = new Scanner(System.in);
        String output = "";
        System.out.println("number: ");
        String input = ui.next();
        while(!input.equals("quit")){
            output+= input + "\n";
            System.out.println("number: ");
            input = ui.next();
        }
        System.out.println(output);
        ui.close();
    }
}