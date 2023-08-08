import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int odd = 0, even = 0, x = 1;
        for(int i=0;i<n;i++) {
            int number = sc.nextInt();
            if (number % 2 == 1) odd++;
            else even++;
        }
        if ((n % 2 == 0 && odd != even) || (n % 2 == 1 && odd - even != 1)) x = 0;
        System.out.println(x);
        sc.close();
        
    }
}
