import java.util.Arrays;
import java.util.Scanner;

public class Main_2444 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N = sc.nextInt();
		int s = (2 * N - 1) / 2;
		String[] arr = new String[N * 2 - 1];
		String str = "";
		arr[s] = "*";
		for (int i = 0; i < N; i++) {
			str = "";
			arr[s + i] = "*";
			arr[s - i] = "*";
			for (int j = 0; j < arr.length; j++) {
				if (arr[j]==null) {
					arr[j] = " ";
					str+=" ";
				}else {
					str+=arr[j];
				}
			}
			System.out.println(str);
//			for(int k=/)
		}
	}

}
