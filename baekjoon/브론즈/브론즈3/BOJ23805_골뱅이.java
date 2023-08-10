import java.util.Scanner;

public class Main {
    public static void BOJ23805_골뱅이(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        for(int i=1 ; i<=n ; i++) {
            System.out.println("@".repeat(3 * n) + " ".repeat(n) + "@".repeat(n));
        }
        for(int i=1 ; i<=3*n ; i++) {
            System.out.println("@".repeat(n) + " ".repeat(n) + "@".repeat(n) + " ".repeat(n) + "@".repeat(n));
        }
        for(int i=1 ; i<=n ; i++) {
            System.out.println("@".repeat(n) + " ".repeat(n) + "@".repeat(3 * n));
        }
        sc.close();
    }
}
