import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args)throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int num = Integer.parseInt(br.readLine());
		
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		int [] n = new int [num];
		for(int i=0; i<num; i++) {
				n[i]=Integer.parseInt(st.nextToken());
		}
		Arrays.sort(n);
		System.out.println(n[0]+" "+n[num-1]);
	}

}
