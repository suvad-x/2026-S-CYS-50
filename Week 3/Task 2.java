```java
class Student {
    void introduce() {
        System.out.println("Hello, everyone!");
    }

    void showName() {
        System.out.println("Name: Suvaid");
    }

    void showAge() {
        System.out.println("Age: 18");
    }

    void showCity() {
        System.out.println("City: Lahore");
    }
}

class Friendship {
    void firstFriend() {
        System.out.println("Friend 1: Ahmed");
    }

    void secondFriend() {
        System.out.println("Friend 2: Hadi");
    }
}

public class task2 {
    public static void main(String[] args) {
        Student s = new Student();
        s.introduce();
        s.showName();
        s.showAge();
        s.showCity();

        Friendship f = new Friendship();
        f.firstFriend();
        f.secondFriend();
    }
}
```