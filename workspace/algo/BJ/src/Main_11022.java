import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main_11022 {

	public static void main(String[] args)throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st;
		int tc = Integer.parseInt(br.readLine());
		for(int i =0; i<tc; i++) {
			st = new StringTokenizer(br.readLine());
			int A =  Integer.parseInt(st.nextToken());
			int B =  Integer.parseInt(st.nextToken());
			bw.write("Case #"+(i+1)+": "+A+" + "+B+" = "+(A+B)+"\n");
		}
		bw.close();
	}

}
