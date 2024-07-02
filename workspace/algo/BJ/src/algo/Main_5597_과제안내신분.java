package algo;

import java.util.Arrays;
import java.util.Scanner;

public class Main_5597_과제안내신분 {

	public static void main(String[] args) {
		//1번부터 30번까지 출석번호
		//특별과제 28명제출
		//그러면 배열사이즈가 30인 배열을 생성하고 해당 수가 들어가면 1을넣는다.
		Scanner sc= new Scanner(System.in);
		int [] stud = new int[30];
		int len =30;
		for(int i =0; i<28; i++) {
			int check = sc.nextInt();
			stud[check-1]=1;
		}
		for(int i=0; i<len; i++) {
			if(stud[i]==0) {
				System.out.println(i+1);
			}
		}
		
		
	}

}
