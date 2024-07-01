import java.util.Scanner;

public class Main_2444_별찍기 {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int N= scan.nextInt();
		//N=5
		for(int i=1; i<N;i++){ //1~5 4번
			System.out.print(" ");
		for(int j=0; j<i*2-1; j++)//i=1> j=0
			System.out.print("*");
			System.out.println();
		}
		for(int i=N-1; i>=0; i--){
			for(int j=0; j<i*2-1; j++)
				System.out.print("*");
				System.out.println();
			}
	}

}
