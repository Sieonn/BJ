package algo;

import java.util.Scanner;

public class Main_11718_그래도출력하기 {

	public static void main(String[] args) {
		// 입력받은 그대로 출력
		Scanner sc = new Scanner(System.in);
		while (sc.hasNextLine()) {
			String str = sc.nextLine();
			System.out.println(str);
		}
		sc.close();
	}

}
