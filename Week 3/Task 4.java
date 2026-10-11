```java
class StudentInfo {
    String studentName;
    int studentAge;
    long studentID;
}

public class task4 {
    public static void main(String[] args) {
        StudentInfo data = new StudentInfo();

        data.studentName = "Suvaid";
        data.studentAge = 18;
        data.studentID = 12345678901L;

        System.out.println("Student Name: " + data.studentName);
        System.out.println("Student Age: " + data.studentAge);
        System.out.println("Student ID: " + data.studentID);
    }
}
```