package algo;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class Main_1931_회의실배정 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int M = scan.nextInt();
		int [] arr= new int[N];
		for(int i =0; i<M; i++) {
			int start = scan.nextInt()-1;
			int end = scan.nextInt();
			int num = scan.nextInt();
			for(int s =start; s<end; s++) {
				arr[s] = num;
			}
		}
		for(int i=0; i<N; i++) {
			System.out.print(arr[i]+" ");
		}
	}

}
