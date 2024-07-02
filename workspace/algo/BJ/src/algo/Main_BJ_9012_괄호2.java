package algo;

import java.util.Scanner;
import java.util.Stack;

public class Main_BJ_9012_괄호2 {

	public static void main(String[] args) {
	//입력
		Scanner sc = new Scanner(System.in);
		int T =sc.nextInt();
		boolean [] check = new boolean[T];
		for(int i=0; i<T; i++) {
			String ps = sc.next();
//			check[i]
		}
	}// End Main
	static boolean VPScheck(String ps) {
		//입력받은 문자열을 Stack을 이용하여 VPS인지 체크
		Stack<Character> stack = new Stack<>();
		
		for(int i=0; i<ps.length(); i++) {
			if(ps.charAt(i)=='(') {
				stack.push(ps.charAt(i));
				break;
			}
			else {
				stack.pop();
			}
		}
		if(stack.isEmpty()) return true;
		else return false;
	}

}// End Class

//2504, 4949, 10799, 1021
