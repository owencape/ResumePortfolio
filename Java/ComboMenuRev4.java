import java.util.Scanner;

public class ComboMenuRev4 {

    public static void main(String[] args) {
        Scanner ui = new Scanner(System.in);

        double total = 0;
       

               while (true) {
            double orderTotal = 0;

            while (true) {
                System.out.println("Menu:");
                System.out.println("1. Sandwich (tofu: $5.75, chicken: $5.25, beef: $6.25)");
                System.out.println("2. Fries (small: $1, medium: $1.75, large: $2.25)");
                System.out.println("3. Drink (small: $1, medium: $1.50, large: $2.00)");

                System.out.print("Enter your choice (sandwich/fries/drink) or 'done' to finish ordering: ");
                String choice = ui.nextLine().toLowerCase();

                if (choice.equals("done")) {
                    break;
                }

                double price = 0;
                String itemName = "";
                boolean validChoice = true;

                if (choice.equals("sandwich")) {
                    System.out.print("Enter your choice for sandwich (tofu/chicken/beef): ");
                    String sandwichChoice = ui.nextLine().toLowerCase();
                    if (sandwichChoice.equals("tofu")) {
                        price = 5.75;
                        itemName = "Tofu Sandwich";
                    } else if (sandwichChoice.equals("chicken")) {
                        price = 5.25;
                        itemName = "Chicken Sandwich";
                    } else if (sandwichChoice.equals("beef")) {
                        price = 6.25;
                        itemName = "Beef Sandwich";
                    } else {
                        validChoice = false;
                    }
                } else if (choice.equals("fries")) {
                    System.out.print("Enter your choice for fries (small/medium/large): ");
                    String friesChoice = ui.nextLine().toLowerCase();
                    if (friesChoice.equals("small")) {
                        price = 1;
                        itemName = "Small Fries";
                    } else if (friesChoice.equals("medium")) {
                        price = 1.75;
                        itemName = "Medium Fries";
                    } else if (friesChoice.equals("large")) {
                        price = 2.25;
                        itemName = "Large Fries";
                    } else {
                        validChoice = false;
                    }
                } else if (choice.equals("drink")) {
                    System.out.print("Enter your choice for drink (small/medium/large): ");
                    String drinkChoice = ui.nextLine().toLowerCase();
                    if (drinkChoice.equals("small")) {
                        price = 1;
                        itemName = "Small Drink";
                    } else if (drinkChoice.equals("medium")) {
                        price = 1.50;
                        itemName = "Medium Drink";
                    } else if (drinkChoice.equals("large")) {
                        System.out.print("Do you want to upgrade to child size for $0.38 more? (yes/no): ");
                        String upgradeChoice = ui.nextLine().toLowerCase();
                        if (upgradeChoice.equals("yes")) {
                            price = 2.38;
                            itemName = "Child Size Drink";
                        } else {
                            price = 2.00;
                            itemName = "Large Drink";
                        }
                    } else {
                        validChoice = false;
                    }
                } else {
                    validChoice = false;
                }

                if (validChoice) {
                    total += price;
                    orderTotal += price;
                    System.out.println("You ordered: " + itemName + " - $" + String.format("%.2f", price));
                } else {
                    System.out.println("Invalid choice. Please try again.");
                }
            }

            System.out.println("\nWould you like to buy ketchup packets for $0.25 each? (yes/no): ");
            String ketchupChoice = ui.nextLine().toLowerCase();
            if (ketchupChoice.equals("yes")) {
                System.out.print("How many ketchup packets would you like to buy? ");
                String amount = ui.nextLine();
                // check for negative or deciamls maybe use a loop

                int numPackets = Integer.parseInt(amount);
                total += 0.25 * numPackets;
                orderTotal += 0.25 * numPackets;
                System.out.println("You ordered " + numPackets + " ketchup packets - $" + String.format("%.2f", 0.25 * numPackets));
            }

            double tax = total*.07;
            double subtotal = total;
            double finalTotal = total*1.07;


            System.out.println("\nOrder Summary:");
            System.out.println("Subtotal cost: $" + String.format("%.2f", subtotal));
            System.out.println("Tax: $" + String.format("%.2f", tax));
            System.out.println("Total cost: $" + String.format("%.2f", finalTotal));

            System.out.println("\nWould you like to place another order? (yes/no): ");
            String anotherOrder = ui.next().toLowerCase();
            if (!anotherOrder.equals("yes")) {
                break;
            }
        }

        double tax = total*.07;
        double subtotal = total;
        double finalTotal = total*1.07;

        System.out.println("\nAll Orders Summary:");
        System.out.println("Subtotal cost for all orders: $" + String.format("%.2f", subtotal));
        System.out.println("Tax for all orders: $" + String.format("%.2f", tax));
        System.out.println("Total cost for all orders: $" + String.format("%.2f", finalTotal));
        System.out.println("Thank you for ordering!");
    }
}