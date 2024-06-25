import java.util.Arrays;
import java.util.Scanner;

public class Main_3052_나머지 {

	public static void main(String[] args) {
		// 두 자연수 A, B
		// 10개 입력받고 42로 나눈 나머지 구하기 그래서 그 나머지가 다른 값이 몇개 있는지 구하기
		Scanner sc = new Scanner(System.in);
		int[] arr = new int[10];
		for (int i = 0; i < 10; i++) {
			int val = sc.nextInt();
			arr[i] = val % 42;
		}
		Arrays.sort(arr);
//		System.out.println(Arrays.toString(arr));
		int p = arr[0];
		int cnt = 1;
//		int [] sol = new int[10];
		for (int i = 1; i < 10; i++) {
			if (p != arr[i]) {
				p=arr[i];
				cnt++;
			}
		}
		System.out.println(cnt);
	}

}
