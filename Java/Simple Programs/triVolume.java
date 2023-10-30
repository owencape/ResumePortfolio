import java.util.Scanner;
import java.lang.Math;

public class triangleVolume {

  public static void main(String[] args) {

    Scanner ui = new Scanner(System.in);

    System.out.println("What is your side length: ");
    double sideLength = ui.nextDouble();
    double formula = (Math.sqrt(3))/4;

    double area = formula*(sideLength*sideLength);
    double volume = area * sideLength;

    System.out.println("Area: " + area + "\nVolume: " + volume);
    
    ui.close();
    
  }
}