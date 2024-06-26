import java.util.Scanner;

public class Main_1152_단어의개수 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine().trim();
		sc.close();
		String[] sarr = str.split(" ");
		if (sarr[0].equals("")) {
			System.out.println(0);
		} else {
			System.out.println(sarr.length);
		}
	}

}
//trim 왼쪽 오른쪽에 있는 공백을 다 제거해준다.