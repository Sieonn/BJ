package algo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_2961_도영이 {

	public static void main(String[] args)throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st;
		
		int S=1;
		int B=0;
		int m =0;
		for(int i=0; i<N; i++) {
			st= new StringTokenizer(br.readLine()," ");
			S *= Integer.parseInt(st.nextToken());
			B += Integer.parseInt(st.nextToken());
			m = S - B;
		}
		
		if(m<0) {
			m= m* -1;
		}
		System.out.println(m);
	}

}
