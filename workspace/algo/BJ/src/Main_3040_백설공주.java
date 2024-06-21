import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main_3040_백설공주 {

	public static void main(String[] args) throws Exception {
		// 주어진 수 7개를 더해서 100이 나오는 조합을 구해라
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		int n = Integer.parseInt(br.readLine());
		int[] arr = new int[9];
		int sum = 0;
		for (int i = 0; i < 9; i++) {
			arr[i] = Integer.parseInt(br.readLine());
			sum += arr[i];
		}

		for (int i = 0; i < 8; i++) {
			for (int j = i + 1; j < 9; j++) {
				int cur = arr[i] + arr[j];
				if ((sum - cur) == 100) {
					arr[i] = 0;
					arr[j] = 0;

					for (int k = 0; k < 9; k++) {
						if (k != i && k != j) {
							System.out.println(arr[k]);
						}
					}
				}

			}

		}

	}

}
