import java.util.*;
public class Main
{
    public static void main(String [ ]args )
    {
        int array [] = {2, 4, 5, 3, 6, 32, 7, 8, 6, 54, 9, 8, 12};
        Scanner a = new Scanner(System.in);
        System.out.print("Enter start index : ");
        int s = a.nextInt();
        System.out.print("Enter your ending number : ");
        int e = a.nextInt();
        System.out.print("Enter your steps = ");
        int step = a.nextInt();
        for (int i = s; i < e ; i+= step)
        {
            System.out.println(array [i]);
        }
    }
}