import java.io.*;
import java.util.StringTokenizer;

public class Main_10951 {

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		String str;
		
		while ((str = br.readLine()) !=null) {
			StringTokenizer st = new StringTokenizer(str, " ");
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());;
			System.out.println(a+b);
		}
		br.close();
	}

}
