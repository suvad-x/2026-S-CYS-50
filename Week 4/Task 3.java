import java.util.HashSet;
import java.util.Random;
import java.util.Scanner;
import java.util.Set;

public class Walker {
    private final String name;
    private int x;
    private int y;

    public Walker(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public boolean move(int dx, int dy, Set<String> hurdles) {
        int nx = x + dx;
        int ny = y + dy;
        if (hurdles.contains(nx + ":" + ny)) {
            System.out.println(name + " encounters hurdle at (" + nx + ":" + ny + ")");
            return false;
        }
        x = nx;
        y = ny;
        return true;
    }

    public String location() {
        return "(" + x + " : " + y + ")";
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random rand = new Random();

        Set<String> hurdles = new HashSet<>();
        hurdles.add("1:2");
        hurdles.add("-1:1");
        hurdles.add("0:-3");
        hurdles.add("2:0");

        Walker ali = new Walker("Ali");
        Walker hasan = new Walker("Hasan");
        int[][] dirs = {{0, 1}, {0, -1}, {-1, 0}, {1, 0}};

        System.out.println("Starting: Ali's Location is = " + ali.location()
                + " Hasan's Location is = " + hasan.location());
        System.out.println("Hasan has Random Movement, Ali follows order");
        System.out.println("Ali commands: ^ up, v down, < left, > right, q quit");

        while (true) {
            System.out.print("Ali: Where should i go now: ");
            char c = sc.next().charAt(0);
            if (c == 'q') {
                break;
            }

            int dx = 0;
            int dy = 0;
            switch (c) {
                case '^':
                    dy = 1;
                    break;
                case 'v':
                    dy = -1;
                    break;
                case '<':
                    dx = -1;
                    break;
                case '>':
                    dx = 1;
                    break;
                default:
                    System.out.println("Invalid command.");
                    continue;
            }

            ali.move(dx, dy, hurdles);
            System.out.println("Ali is at = " + ali.location());

            int[] d = dirs[rand.nextInt(4)];
            hasan.move(d[0], d[1], hurdles);
            System.out.println("Hasan is at = " + hasan.location());
        }
        System.out.println("Walk finished.");
    }
}