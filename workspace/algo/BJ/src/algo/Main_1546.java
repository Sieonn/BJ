package algo;

import java.util.Arrays;
import java.util.Scanner;

public class Main_1546 {

	public static void main(String[] args) {
		//최댓값 M
		//모든 점수: 점수/M*100
		Scanner sc= new Scanner(System.in);
		int N = sc.nextInt();
		int [] score = new int [N];
		for(int i=0; i<N; i++) {
			score[i]=sc.nextInt();
		}
		Arrays.sort(score);
		int M=score[N-1];
		double avg =0;
		int [] fake = new int [N];
		for(int j=0; j<N; j++) {
			avg+=(double)score[j]/M*100;
		}
		avg= avg/N;
		System.out.println(avg);
	}

}
