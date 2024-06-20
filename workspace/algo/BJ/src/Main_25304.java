import java.util.Scanner;

public class Main_25304 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int totalprice = sc.nextInt();
		int count = sc.nextInt();
		int sum=0;
		for(int i=0; i<count; i++) {
			int a = sc.nextInt();//물건의 가격
			int b = sc.nextInt();//물건의 개수
			sum+= a*b;
		}
		if(sum==totalprice) {
			System.out.println("Yes");
		}else
		System.out.println("No");
	}

}
