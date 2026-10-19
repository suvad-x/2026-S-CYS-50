public class JTime {
    private int hour;
    private int minute;
    private int second;

    public JTime() {
        this(0, 0, 0);
    }

    public JTime(int hour, int minute, int second) {
        setHour(hour);
        setMinute(minute);
        setSecond(second);
    }

    public JTime(int totalSeconds) {
        totalSeconds = ((totalSeconds % 86400) + 86400) % 86400;
        this.hour = totalSeconds / 3600;
        this.minute = (totalSeconds % 3600) / 60;
        this.second = totalSeconds % 60;
    }

    public int getHour() {
        return hour;
    }

    public int getMinute() {
        return minute;
    }

    public int getSecond() {
        return second;
    }

    public void setHour(int hour) {
        this.hour = (hour >= 0 && hour < 24) ? hour : 0;
    }

    public void setMinute(int minute) {
        this.minute = (minute >= 0 && minute < 60) ? minute : 0;
    }

    public void setSecond(int second) {
        this.second = (second >= 0 && second < 60) ? second : 0;
    }

    public int toSeconds() {
        return hour * 3600 + minute * 60 + second;
    }

    public int elapsedSeconds(JTime other) {
        return Math.abs(this.toSeconds() - other.toSeconds());
    }

    public JTime elapsedTime(JTime other) {
        return new JTime(elapsedSeconds(other));
    }

    @Override
    public String toString() {
        return String.format("%02d:%02d:%02d", hour, minute, second);
    }

    public static void main(String[] args) {
        JTime t1 = new JTime(10, 30, 15);
        JTime t2 = new JTime(8, 15, 45);
        JTime t3 = new JTime();
        JTime t4 = new JTime(37815);

        System.out.println("t1 = " + t1);
        System.out.println("t2 = " + t2);
        System.out.println("t3 (default) = " + t3);
        System.out.println("t4 (from 37815 seconds) = " + t4);
        System.out.println("Elapsed seconds between t1 and t2 = " + t1.elapsedSeconds(t2));
        System.out.println("Elapsed time between t1 and t2 = " + t1.elapsedTime(t2));
    }
}