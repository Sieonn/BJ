import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.Scanner;

public class Main_11047_동전0 {
	public static void main(String[] args) {
		//동전 종류 N
		//동전을 사용해서 합을 K로 만들고 싶음
		//동전 갯수의 최솟값구하기
		Scanner scan = new Scanner(System.in);
		String str = scan.nextLine();
		String [] num =  str.split(" ");
		int N = Integer.parseInt(num[0]);
		int K = Integer.parseInt(num[1]);
		
		Integer [] val = new Integer [N];
		for(int i=0; i<N; i++) {
			val[i] = scan.nextInt();
		}
//		Arrays.sort(val);//오름차순
		Arrays.sort(val,Collections.reverseOrder());
//		System.out.println(Arrays.toString(val));
		int h=0;
		for(int j = 0; j<N; j++) {
			if(K%val[j]<K) {
//				System.out.println(K/val[j]+" "+ val[j]);
				h+=K/val[j];
				K-=val[j]*(K/val[j]);
//				System.out.println(h);
			}
		}
		System.out.println(h);
	}
}
