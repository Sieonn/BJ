package algo;

import java.util.Arrays;
import java.util.Scanner;

public class Main_2294_동전2 {

	public static void main(String[] args) {
		//n가지 종류의 동전이있는데 적당히 합쳐서 k원이 되면서 동전 개수가 최소
		Scanner sc= new Scanner(System.in);
		int n = sc.nextInt(); //동전 종류 갯수
		int k = sc.nextInt();
		int [] val= new int [n];
		for(int i=0; i<n; i++) {
			val[i] = sc.nextInt();
		}
		System.out.println(Arrays.toString(val));
		//출력해야할 것 최소로 사용한것
		int cnt=0;
		int i =0;
		int j=0;
		int [] cnt2 = new int [n];
		while(k>0) {
			cnt +=k/val[i];
			k -= cnt*val[i];
			if(k==0) {
				cnt2[j] = cnt;
				j++;
				cnt =0;
			}else if(k<0) {
				System.out.println(-1);
			}
			i++;
			
		}
		Arrays.sort(cnt2);
		System.out.println(Arrays.toString(cnt2));
		
	}

}
