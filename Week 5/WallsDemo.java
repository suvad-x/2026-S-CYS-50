import java.util.Scanner;

class Walls {
    private String flavor;
    private int scoops;
    private String coneType;
    private int price;

    private static final int PRICE_PER_SCOOP = 75;
    private static final int WAFFLE_EXTRA = 40;

    // Defaults: Vanilla, 1 scoop, Sugar cone
    public Walls() {
        this("Vanilla", 1, "Sugar");
    }

    public Walls(String flavor, int scoops, String coneType) {
        this.flavor = flavor;
        this.scoops = scoops;
        this.coneType = coneType;
        this.price = scoops * PRICE_PER_SCOOP;
        if (coneType.equalsIgnoreCase("Waffle")) {
            this.price += WAFFLE_EXTRA;
        }
    }

    public String getFlavor() { return flavor; }
    public int getScoops() { return scoops; }
    public String getConeType() { return coneType; }
    public int getPrice() { return price; }

    public void display() {
        System.out.println("Flavor : " + flavor);
        System.out.println("Scoops : " + scoops);
        System.out.println("Cone   : " + coneType);
        System.out.println("Price  : Rs. " + price);
    }
}

public class WallsDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Flavors:");
        System.out.println("1. Chocolate");
        System.out.println("2. Vanilla");
        System.out.println("3. Strawberry");
        System.out.println("4. Mango");
        System.out.println("5. Tutti Fruit");
        System.out.println("6. Almond Crunch");
        System.out.println("7. Coffee");
        System.out.print("Choose flavor (1-7): ");
        int f = sc.nextInt();

        String flavor;
        switch (f) {
            case 1: flavor = "Chocolate"; break;
            case 2: flavor = "Vanilla"; break;
            case 3: flavor = "Strawberry"; break;
            case 4: flavor = "Mango"; break;
            case 5: flavor = "Tutti Fruit"; break;
            case 6: flavor = "Almond Crunch"; break;
            case 7: flavor = "Coffee"; break;
            default:
                System.out.println("Invalid flavor, using default (Vanilla).");
                flavor = "Vanilla";
        }

        System.out.print("Number of scoops: ");
        int scoops = sc.nextInt();
        if (scoops < 1) {
            System.out.println("Invalid scoops, using 1.");
            scoops = 1;
        }

        System.out.print("Cone type (1 = Sugar, 2 = Waffle): ");
        int c = sc.nextInt();
        String cone;
        switch (c) {
            case 2: cone = "Waffle"; break;
            case 1: cone = "Sugar"; break;
            default:
                System.out.println("Invalid cone, using Sugar.");
                cone = "Sugar";
        }

        System.out.println("\n--- Your Order ---");
        new Walls(flavor, scoops, cone).display();

        System.out.println("\n--- Default Order ---");
        new Walls().display();

        sc.close();
    }
}
