package algo;

import java.util.Arrays;
import java.util.Scanner;

public class Main_9086 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();
		int num=0;
		for (int i = 0; i < tc; i++) {
			String str = sc.next();
			String [] sarr = str.split("");
			System.out.println(sarr[0] + sarr[sarr.length-1] );
		}
	}

}
