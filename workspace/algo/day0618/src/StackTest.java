import java.util.Stack;

public class StackTest {

	public static void main(String[] args) {

		Stack<String> stack = new Stack<String>();
		System.out.println("스택의 요소 개수:"+stack.size()+", 스택Empty체크:"+ 
		stack.isEmpty());
		stack.push("홍길동");
		stack.push("김주원");
		stack.push("길라임");
		System.out.println("스택의 요소 개수:"+stack.size()+", 스택Empty체크:"+stack.isEmpty());
		
		System.out.println(stack.pop());//길라임
		System.out.println(stack.peek());//김주원
		System.out.println("스택의 요소 개수:"+stack.size()+", 스택 Empty체크:"+stack.isEmpty());
		
		System.out.println(stack.pop());//김주원
		System.out.println(stack.pop());//홍길동
//		System.out.println(stack.pop());//에러발생: EmptyStackException 요소가 없는데 pop을 시키면 에러가 발생한다.
		System.out.println(stack.peek());//에러발생: EmptyStackException 요소가 없는데 peek을 시키면 에러가 발생한다.
		//실행도중에 에러가 나는 경우는 try-catch가 아니라 if로 처리한다.
	
	
	}

}
