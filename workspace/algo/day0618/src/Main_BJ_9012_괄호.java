import java.util.Scanner;
import java.util.Stack;

public class Main_BJ_9012_괄호 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int tc = sc.nextInt();
		
		Stack<Character> stack = new Stack<>();

		for (int i = 0; i < tc; i++) {
			String str = sc.next();
			int len = str.length();
			for (int j = 0; j < len; j++) {
				char ch = str.charAt(j);

				if (ch == '(') {
					stack.push(ch);
				} else {
					int size = stack.size();
					if (size == 0) {
						stack.push(ch);
						break;
					} else {
						stack.pop();
					}
				}
			}
			if (stack.isEmpty()) {
				System.out.print("\n"+ "YES");
			} else {
				System.out.print("\n"+ "NO");
			}
			stack.clear();
		}
	}// End Main

}// End Class

//2504, 4949, 10799, 1021
