package algo;

import java.util.Scanner;

public class Main_2675_문자열반복 {

	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		int N = sc.nextInt();

		for(int i=0; i<N; i++) {
			int S = sc.nextInt();
			String str = sc.next().trim();
			String [] arr = str.split("");
			String sol="";
			for(int j=0; j<str.length(); j++) {
				for(int k=0; k<S; k++) {
					sol+=arr[j];
				}
			}
			System.out.println(sol);
		}
	}

}
