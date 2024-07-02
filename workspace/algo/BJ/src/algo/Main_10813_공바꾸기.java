package algo;

import java.util.Arrays;
import java.util.Scanner;

public class Main_10813_공바꾸기 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int M = sc.nextInt();
		int[]arr =  new int[N];
		for(int i=0; i<N; i++) {
			arr[i] = i+1;
		}
		int temp;
		for(int i=0;i<M; i++) {
			int s = sc.nextInt()-1;
			int d = sc.nextInt()-1;
			temp = arr[s];
			arr[s] =arr[d];
			arr[d] = temp; 
		}
		for(int data: arr) {
			System.out.print(data+" ");
		}
	}

}
