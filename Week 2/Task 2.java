import java.util.*;
public class Main
{
    public static void main(String [ ]args )
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your minutes : ");

        int minutes = sc.nextInt();
        int hours = minutes/60;
        int remainingminutes = hours % 60;
        System.out.println(minutes);
        sc.close();

    }
}