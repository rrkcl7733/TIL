import java.util.Scanner;

public class BOJ23925_Retype {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long t = sc.nextLong();
        for (int i=0;i<t;i++) {
            long n = sc.nextLong();
            long k = sc.nextLong();
            long s = sc.nextLong();
            long t1 = n + k, t2 = n + 2 * k - 2 * s;
            System.out.println("Case #" + (i+1) + ": " + Math.min(t1, t2));
        }
    }
}
