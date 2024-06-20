import java.util.Scanner;

public class Main_BJ_2739_구구단 {

	public static void main(String[] args) {
		Scanner scan =  new Scanner(System.in);
		int N =  scan.nextInt();
		for(int i=1; i<=9; i++) {
			System.out.println(N+" * "+i+" = "+N*i);
		}
	}

}
