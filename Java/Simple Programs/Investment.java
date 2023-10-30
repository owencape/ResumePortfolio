import java.util.Scanner;
import java.lang.Math;

public class Investment {
    public static void main(String[] args) {

        Scanner ui = new Scanner(System.in);
        System.out.println("What's your investment? ");
        double invest = ui.nextDouble();
        System.out.println("What's your annual interest rate? ");
        double rate = ui.nextDouble();
        System.out.println("How many years? ");
        double years = ui.nextDouble();

        rate ++;
        years*=12;

        System.out.printf("Future money: %s",invest*Math.pow(rate, years));
        
    }
}
