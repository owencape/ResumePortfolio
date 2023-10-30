import java.util.Scanner;
import java.util.Random;

public class MadLib {

   public static void main(String[] args) {
    
    Scanner ui = new Scanner(System.in);
    System.out.println("Adjective: ");
    String adj1 = ui.nextLine();
    System.out.println("Adjective: ");
    String adj2 = ui.nextLine();
    System.out.println("Type of Bird: ");
    String bird = ui.nextLine();
    System.out.println("Room in a House: ");
    String room = ui.nextLine();
    System.out.println("Verb (past tense): ");
    String verb = ui.nextLine();
    System.out.println("Random Name: ");
    String rname = ui.nextLine();
    System.out.println("Noun: ");
    String noun = ui.nextLine();
    System.out.println("A liquid: ");
    String liquid = ui.nextLine();
    System.out.println("Verb ending in -ing: ");
    String verbing = ui.nextLine();
    System.out.println("Part of body (plural): ");
    String part = ui.nextLine();
    System.out.println("Plural Noun: ");
    String pnoun = ui.nextLine();
    System.out.println("Verb ending in -ing: ");
    String verbing2 = ui.nextLine();
    System.out.println("Noun: ");
    String Noun2 = ui.nextLine();
 

    System.out.printf("It was a %s, cold November Day. I woke up to the %s smell of %s roasting in the %s down the stairs to see if I could help %s the dinner. My mom said, See if %s needs a fresh %s So I carried a tray of glasses full of %s into the %s room. When I got there, I couldn't believe my %s! There were %s %s on the %s!" , adj1,adj2,bird,room,verb,rname,noun,liquid,verbing,part,pnoun,verbing2,Noun2);


   } 
}