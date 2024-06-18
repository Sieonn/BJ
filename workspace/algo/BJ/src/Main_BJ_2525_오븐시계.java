import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_BJ_2525_오븐시계 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine();
		StringTokenizer tokens = new StringTokenizer(str," ");
		int hour = Integer.parseInt(tokens.nextToken());
		int minute = Integer.parseInt(tokens.nextToken());
		int timer = Integer.parseInt(br.readLine());

		minute+=timer;
		if(minute>60) {
			hour+= minute/60;
			minute = minute%60;
		}
		
		if(hour==24) {
			hour =0;
		}else if(hour >24) {
			hour-=24;
		}
		System.out.println(hour +" "+minute);
	}

}// 틀림
