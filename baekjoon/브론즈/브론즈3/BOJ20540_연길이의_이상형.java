import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		
		String a = String.valueOf(str.charAt(0)).equals("I")? "E": "I";
		String b = String.valueOf(str.charAt(1)).equals("N")? "S": "N";
		String c = String.valueOf(str.charAt(2)).equals("F")? "T": "F";
		String d = String.valueOf(str.charAt(3)).equals("P")? "J": "P";
		System.out.println(a + b + c + d);
		sc.close();
	}
}
