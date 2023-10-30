import java.util.Scanner;

public class minuteToYear {

  public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);
        
        System.out.println("How many minutes: ");

        int minutes = ui.nextInt();
        int initial = minutes;

        int days = 0;
        int years = 0;
        

        while (minutes >= 525600){
            minutes -= 525600;
            years += 1;
        }

        while (minutes >= 1440){
            minutes -= 1140;
            days += 1;
        }

        System.out.printf("%s minutes is the same as %s years & %s days!!!",initial,years,days);

        ui.close();
  }
}