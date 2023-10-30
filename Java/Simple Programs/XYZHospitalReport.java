import java.util.Scanner;

public class XYZHospitalReport {
  public static void main(String[] args) {

    Scanner ui = new Scanner(System.in);

    System.out.println("Please enter your first name?");
    String firstName = ui.nextLine();
    
    System.out.println("Please enter your last name?");
    String lastName = ui.nextLine();

    System.out.println("Please enter your address?");
    String address = ui.nextLine();

    System.out.println("Please enter your city?");
    String city = ui.nextLine();

    System.out.println("Please enter your state?");
    String state = ui.nextLine();

    System.out.println("Please enter your zip code?");
    String zipCode = ui.nextLine();

    System.out.println("Please enter your amount owed?");
    String owed = ui.nextLine();

    System.out.println("Please enter your payment amount?");
    String payment = ui.nextLine();
    System.out.println("Please enter your payment date?");
    String payDate = ui.nextLine();

    System.out.println("----------------------------------------------------------------------------------------------");
    System.out.println("Name              Address               Payment Information");
    System.out.printf("Last\tFirst\tAddress\t\t\tCity,State\tZip\t Amount Owed\tAmount Paid\tPaid Date\n");
    System.out.printf("%s\t%s\t%s\s%s,%s\t%s\t\t$%s\t$%s\t%s%n",lastName,firstName,address,city,state,zipCode,owed,payment,payDate );
    System.out.println("----------------------------------------------------------------------------------------------");
    
    ui.close();
  }
}