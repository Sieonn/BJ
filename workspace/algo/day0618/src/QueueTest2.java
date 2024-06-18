import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;
import java.util.Scanner;

public class QueueTest2 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int totalCandies = sc.nextInt();
		Queue<Integer> queue = new ArrayDeque<>();
		ArrayList<Integer> candyS = new ArrayList<>();

		while (totalCandies > 0) {
			if (queue.isEmpty()) {
				queue.add(1);
				candyS.add(0, 1);
				totalCandies -=1;
				System.out.println(queue + " " + candyS.size() + " " + +totalCandies);
			} else {
				int returnP = queue.peek();
				queue.add(queue.poll());
				queue.add(queue.size() + 1);
				if (candyS.size() != returnP) {
					candyS.add(1);
				} else {
					int num = candyS.get(returnP - 1);
					candyS.set(returnP - 1, candyS.get(returnP - 1) + 1);
				}
				totalCandies -= candyS.get(returnP - 1);
				System.out.println(queue + " " + candyS.size() + " " + +totalCandies);
				for (int i = 0; i < candyS.size(); i++) {
					System.out.print(candyS.get(i) + " ");
				}
			}
		}
		System.out.println("마지막 캔디를 받은 사람은 " + queue.peek() + "째 입니다.");
	}

}

//1
//12
//213
//1324
//32415