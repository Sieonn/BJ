import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;
import java.util.Scanner;

public class QueueTest {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int totalCandies = sc.nextInt();
		Queue<Integer> queue = new ArrayDeque<>();
		ArrayList<Integer> candyS = new ArrayList<>();

		while (totalCandies > 0) {
			if (queue.isEmpty()) {
				queue.add(1);
				candyS.add(1);
				totalCandies -=1;
				System.out.println(queue + " " + candyS.size() + " " + +totalCandies);
			} else {
				queue.add(queue.poll());
				queue.add(queue.size() + 1);
				int returnP = queue.peek();
				if (candyS.size() < returnP){
					candyS.add(1);
				} else {
					candyS.set(returnP - 1, candyS.get(returnP - 1) + 1);
				}
				totalCandies -= candyS.get(returnP - 1);
				System.out.println(queue + " " +returnP +candyS.get(returnP - 1) + " " + +totalCandies);
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

//import java.util.LinkedList;
//import java.util.Queue;
//
//public class CandyQueue {
//    public static void main(String[] args) {
//        int totalCandies = 20;
//        Queue<Person> queue = new LinkedList<>();
//        
//        // 초기 상태: 1번만 줄을 섬
//        queue.add(new Person(1, 0));
//        int currentCandy = 0;
//        
//        while (currentCandy < totalCandies) {
//            // 줄의 첫 번째 사람을 가져옴
//            Person person = queue.poll();
//            
//            // 캔디를 받음
//            person.candyCount++;
//            currentCandy += person.candyCount;
//            
//            // 다시 줄을 섬
//            queue.add(person);
//            
//            // 새로운 사람이 줄을 섬
//            if (queue.size() <= totalCandies - currentCandy) {
//                queue.add(new Person(queue.size() + 1, 0));
//            }
//            
//            // 마지막 캔디를 받는 사람을 출력
//            if (currentCandy >= totalCandies) {
//                System.out.println("마지막 캔디를 받은 사람: " + person.id + "번");
//            }
//        }
//    }
//}
//
//class Person {
//    int id;
//    int candyCount;
//    
//    public Person(int id, int candyCount) {
//        this.id = id;
//        this.candyCount = candyCount;
//    }
//}
