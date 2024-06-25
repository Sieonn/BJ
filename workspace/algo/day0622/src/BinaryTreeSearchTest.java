
public class BinaryTreeSearchTest {

	public static void main(String[] args) {
		int size = 9;
		
		BinaryTreeSearch<Character> tree = new BinaryTreeSearch<>(9);
		
		//'A'부터 9개의 문자를 저장!
		for(int i=0; i<9; i++) {
			tree.add((char)(65+i));
		}
		
		tree.bfs(); //이진트리에 대한
	}//main

}
