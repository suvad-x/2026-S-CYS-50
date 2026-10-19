import java.util.Scanner;

public class SavingAccount {
    private double balance;

    public SavingAccount(double initialBalance) {
        balance = Math.max(initialBalance, 0);
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Deposited: " + amount);
        } else {
            System.out.println("Invalid amount.");
        }
    }

    public void withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Invalid amount.");
        } else if (amount > balance) {
            System.out.println("Insufficient balance.");
        } else {
            balance -= amount;
            System.out.println("Withdrawn: " + amount);
        }
    }

    public void checkBalance() {
        System.out.println("Current balance: " + balance);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        SavingAccount acc = new SavingAccount(1000);
        int choice;

        do {
            System.out.println("\n--- Bank Menu ---");
            System.out.println("1. Deposit money");
            System.out.println("2. Withdraw money");
            System.out.println("3. Check balance");
            System.out.println("4. Exit");
            System.out.print("Enter choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    System.out.print("Amount to deposit: ");
                    acc.deposit(sc.nextDouble());
                    break;
                case 2:
                    System.out.print("Amount to withdraw: ");
                    acc.withdraw(sc.nextDouble());
                    break;
                case 3:
                    acc.checkBalance();
                    break;
                case 4:
                    System.out.println("Goodbye.");
                    break;
                default:
                    System.out.println("Invalid choice.");
            }
        } while (choice != 4);
    }
}