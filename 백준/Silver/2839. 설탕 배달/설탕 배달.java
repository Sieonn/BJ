import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		//N키로 배달해야함
		//3	5
		Scanner scan = new Scanner(System.in);
		int N = scan.nextInt();
		int cnt = 0;
		while(N>0) {
			if(N%5==0) { //5의 배수
			cnt+=N/5;
			break;
			}else{
				N-=3;
				cnt++;
			}if(N<0) {
				cnt= -1;
			}
		}
		System.out.println(cnt);
	}

}