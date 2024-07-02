package algo;

import java.util.Arrays;
import java.util.Scanner;

public class Main_2908_상수 {

	public static void main(String[] args) {
		// 두 수가 주어지는데 이들의 순서를 거꾸로해서 큰수 출력
		Scanner sc = new Scanner(System.in);
		String A = sc.next();
		String [] arrA = A.split(""); 
		String B = sc.next();
		String [] arrB = B.split(""); 

		A="";
		B="";
		for(int i=2; i>=0; i--){
			A +=arrA[i];
			B +=arrB[i];
		}
		int M = Math.max(Integer.parseInt(A), Integer.parseInt(B));
		System.out.println(M);
		
//		System.out.println(Arrays.toString(arrA));
//		System.out.println(Arrays.toString(arrB));
	}

}
