class DayType {
    private static final String[] DAYS = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"};
    private int dayIndex;

    public DayType() {
        dayIndex = 0;
    }

    public DayType(String day) {
        setDay(day);
    }

    // a. Set the day (accepts "Mon" or "Monday", any case)
    public void setDay(String day) {
        String key = day.trim().toLowerCase();
        if (key.length() < 3) {
            throw new IllegalArgumentException("Invalid day: " + day);
        }
        for (int i = 0; i < DAYS.length; i++) {
            if (key.startsWith(DAYS[i].toLowerCase())) {
                dayIndex = i;
                return;
            }
        }
        throw new IllegalArgumentException("Invalid day: " + day);
    }

    // b. Print the day
    public void printDay() {
        System.out.println("Day: " + DAYS[dayIndex]);
    }

    // c. Return the day
    public String getDay() {
        return DAYS[dayIndex];
    }

    // d. Return the next day
    public String nextDay() {
        return DAYS[(dayIndex + 1) % 7];
    }

    // e. Return the previous day
    public String previousDay() {
        return DAYS[(dayIndex + 6) % 7];
    }

    // f. Return the day after adding n days
    public String addDays(int n) {
        int idx = ((dayIndex + n) % 7 + 7) % 7; // also handles negative n
        return DAYS[idx];
    }
}

public class DayTypeDemo {
    public static void main(String[] args) {
        DayType d = new DayType();
        d.setDay("Mon");
        d.printDay();
        System.out.println("Return day: " + d.getDay());
        System.out.println("Next day: " + d.nextDay());
        System.out.println("Previous day: " + d.previousDay());
        System.out.println("Mon + 4 days = " + d.addDays(4));

        d.setDay("Tue");
        System.out.println("Tue + 13 days = " + d.addDays(13));
    }
}
