import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception {
		BufferedReader br= new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		String str = br.readLine();
		StringTokenizer st = new StringTokenizer(str," ");
		int v = Integer.parseInt(br.readLine());
		int count = 0;
		for(int i=0; i<n; i++) {
			int st1 = Integer.parseInt(st.nextToken());
			if(v==st1) {
				count++;
			}
		}
		System.out.println(count);
	}

}
