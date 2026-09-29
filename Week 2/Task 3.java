import java.util.*;
public class Main
{
    public static void main(String [ ]args )
    {
        Scanner suvad = new Scanner (System.in);
        System.out.print("Enter your time in minutes : ");
        int minutes = suvad.nextInt();
        int hours = 12 + minutes / 60;
        int remainingMinutes = minutes % 60;
        System.out.print("Time is = ");
        System.out.println(hours +":"+ remainingMinutes);
        suvad.close();
    }
}