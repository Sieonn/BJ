import java.util.Scanner;

public class Main_25314 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n= sc.nextInt();
		int num =  n/4;
		String str = "";
		for(int i = 0; i<num; i++ ) {
			str += "long ";
		}
		System.out.println(str+"int");
	}

}
