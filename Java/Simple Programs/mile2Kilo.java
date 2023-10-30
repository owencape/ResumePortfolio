import java.util.Scanner;

public class mile2Kilo {
    public static void main(String[] args) {
        
        Scanner ui = new Scanner(System.in);
        System.out.println("How many miles?");
        double miles = ui.nextDouble();
        

        double kilo = miles*1.609344;

        System.out.printf("Kilometers: "+ kilo);
        ui.close();



    }
}
