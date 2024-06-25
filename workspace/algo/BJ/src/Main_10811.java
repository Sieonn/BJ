import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_10811 {

	public static void main(String[] args)throws Exception {
		//바구니 총 N개보유
		//역순으로 만들 M횟수
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		String str =  br.readLine();
		StringTokenizer st =  new StringTokenizer(str, " ");
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int [] arr = new int[N];
		int [] arr2 = new int[N];
		for(int i=0; i<N; i++) {
			arr[i] =i+1;
		}
		
		for(int i =0; i<M; i++) {
			String num = br.readLine();
			st = new StringTokenizer(num," ");
			int start= Integer.parseInt(st.nextToken());
			int end= Integer.parseInt(st.nextToken());
			for(int j=end; j>=start; j--) {
				arr[j] = arr2[end-start];
			}
		}
		
	}

}
