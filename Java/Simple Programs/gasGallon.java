import java.util.Scanner;

public class gasGallon {
    public static void main(String[] args) {

        Scanner ui = new Scanner(System.in);

        System.out.println("Driving distance (miles) ?");
        double miles = ui.nextDouble();

        System.out.println("What is your miles per gallon? ");
        double mpg = ui.nextDouble();

        System.out.println("What's the cost of gas per gallon? ");
        double cost = ui.nextDouble();

        double finalEff = (miles/mpg) * cost;

        System.out.printf("$%2.2f%n",finalEff);

        ui.close();
    }
}
