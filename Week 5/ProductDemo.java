import java.util.Scanner;

class Product {
    private String name;
    private int price;
    private int quantity;

    private static int totalProduct = 0;

    public Product() {
        name = "Unknown";
        price = 0;
        quantity = 0;
        counter();
    }

    public Product(String name, int price, int quantity) {
        this.name = name;
        this.price = price;
        this.quantity = quantity;
        counter();
    }

    // Reads product data from the user
    public void getData() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter name: ");
        name = sc.nextLine();
        System.out.print("Enter price: ");
        price = sc.nextInt();
        System.out.print("Enter quantity: ");
        quantity = sc.nextInt();
    }

    public void display() {
        System.out.println("Name: " + name + ", Price: " + price + ", Quantity: " + quantity);
    }

    // Increments the static counter
    public static void counter() {
        totalProduct++;
    }

    public static int countProduct() {
        return totalProduct;
    }
}

public class ProductDemo {
    public static void main(String[] args) {
        Product p1 = new Product();
        Product p2 = new Product("Pen", 20, 100);
        Product p3 = new Product("Notebook", 150, 50);
        Product p4 = new Product("Bag", 1200, 10);
        Product p5 = new Product();

        p1.display();
        p2.display();
        p3.display();
        p4.display();
        p5.display();

        System.out.println("Total products: " + Product.countProduct());
    }
}
