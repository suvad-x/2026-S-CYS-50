```java
class StudentData {
    private String studentName;
    private int studentAge;
    private long identityNumber;

    public void assignName(String n) {
        studentName = n;
    }

    public String retrieveName() {
        return studentName;
    }

    public void assignAge(int a) {
        studentAge = a;
    }

    public int retrieveAge() {
        return studentAge;
    }

    public void assignID(long id) {
        identityNumber = id;
    }

    public long retrieveID() {
        return identityNumber;
    }
}

public class task3_Encapsulation {
    public static void main(String[] args) {
        StudentData student = new StudentData();

        student.assignName("Suvaid");
        student.assignAge(18);
        student.assignID(12345678901L);

        System.out.println("Name: " + student.retrieveName());
        System.out.println("Age: " + student.retrieveAge());
        System.out.println("ID: " + student.retrieveID());
    }
}
```