import java.util.Scanner;

public class EnergyAndWater {
    public static void main(String[] args) {
        
        Scanner ui = new Scanner(System.in);
        System.out.println("How much water(kg)?");
        double water = ui.nextDouble();
        System.out.println("Initial Temp?");
        double initial = ui.nextDouble();
        System.out.println("Final Temp?");
        double fin = ui.nextDouble();


        
        System.out.printf("Energy(J): %s",water*(fin-initial)*4184);
        ui.close();

    }
}
