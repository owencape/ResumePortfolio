
/**
 * GpaCalc
 */
import java.util.Scanner;
import java.lang.Math;



public class GpaCalc {

    public static void main(String[] args) {
        
        Scanner ui = new Scanner(System.in);
        System.out.println("Enter a grade");
        double num1 = ui.nextDouble();
        System.out.println("Enter a grade");
        double num2 = ui.nextDouble();
        System.out.println("Enter a grade");
        double num3 = ui.nextDouble();
        System.out.println("Enter a grade");
        double num4 = ui.nextDouble();

        double gpa = num1 + num2 +num3 + num4;

        System.out.printf("GPA: "+ gpa/4);
        ui.close();



    }
}