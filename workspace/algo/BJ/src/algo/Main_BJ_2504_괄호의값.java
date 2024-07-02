package algo;

import java.util.Scanner;
import java.util.Stack;

public class Main_BJ_2504_괄호의값 {

	public static void main(String[] args) {
		//():2, []:3 안에 있으면 곱하기, ()[]이렇게 옆에 있으면 더하기
	
	Scanner sc= new Scanner(System.in);
	Stack<Character> stack = new Stack<>();
	String str = sc.next();
	int len = str.length();
	int a = 1;
	for(int i=0; i<len; i++) {
		char ch = str.charAt(i);
		if(ch=='(') {
			stack.push(ch);
		}else if(ch=='[') {
			stack.push(ch);
		}else if(ch==')') {
			
		}
	}
	}
}
