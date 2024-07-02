package algo;

import java.util.Scanner;

public class Main_2480_주사위세개 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a = scan.nextInt();
		int b = scan.nextInt();
		int c = scan.nextInt();

		if (a == b && a == c && b == c) {
			System.out.println(10000 + a * 1000);
		} else if (a == b && a != c || a == c && a != b) {
			System.out.println(1000 + a * 100);
		} else if (c == b && c != a) {
			System.out.println(1000 + c * 100);
		} else {
			int d = Math.max(Math.max(a, b), c);
			System.out.println(d * 100);
		}
	}
}
