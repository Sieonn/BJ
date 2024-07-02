package algo;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_10871 {

	public static void main(String[] args)throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String nums = br.readLine();
		StringTokenizer stt = new StringTokenizer(nums," ");
		int [] num = new int[Integer.parseInt(stt.nextToken())];
		int x = Integer.parseInt(stt.nextToken());
		int [] n  = new int[num.length];
		StringBuilder sb = new StringBuilder();
		String str = br.readLine();
		StringTokenizer  st = new StringTokenizer(str," "); 
		for(int i=0; i<num.length; i++) {
			n[i] = Integer.parseInt(st.nextToken());
			if(n[i]<x) {
				sb.append(n[i]).append(" ");
			}
		}
		System.out.println(sb);
		
	}

}
