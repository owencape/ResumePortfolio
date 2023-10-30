import java.util.Scanner;

/**
 * 4FunctionCalc
 */
public class FunctionCalc {

    public static void main(String[] args) {
        
        Scanner ui = new Scanner(System.in);
        System.out.println("Enter a number");
        int num1 = ui.nextInt();
        ui.nextLine();
        System.out.println("Enter an operator");
        String operator = ui.nextLine();
        System.out.println("Enter a number");
        int num2 = ui.nextInt();

if(operator.equals("+")){
            System.out.println(num1+num2);
        }

        else if(operator.equals("-")){
            System.out.println(num1-num2);
        }

        else if(operator.equals("*")){
            System.out.println(num1*num2);
        }

        else if(operator.equals("+")){
            System.out.println(num1/num2);
        }

    }
}