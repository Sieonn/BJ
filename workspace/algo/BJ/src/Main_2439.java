import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main_2439 {

	public static void main(String[] args)throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		
		String str = "";
		for(int i=1; i<=n; i++) {
		int space = n-i;
		for(int j=0; j<space; j++) {
			str+=" ";
		}
		for(int k=0; k<i; k++) {
			str+="*";
		}
		bw.write(str+"\n");
		str ="";
		}
		bw.close();
	}

}
