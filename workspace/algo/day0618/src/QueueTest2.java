import java.util.LinkedList;
import java.util.Queue;
import java.util.Queue;

public class QueueTest2 {
//int []person = new int[]{1,1};을 표현!
	static class Person {
		int no; // 배열 person[0]번지
		int candycnt;// 배열 person[1]번지

		public Person(int no, int candyCnt) {
			super();
			this.no = no;
			this.candycnt = candycnt;

		}

		@Override
		public String toString() {
			return "Person [no=" + no + ", candycnt=" + candycnt + "]";
		}

	}

	public static void main(String[] args) {
		Queue<Person> queue = new LinkedList<>(); // ==> 대기열
//		Queue<int[]> queue = new LinkedList<int[]>();//주소값을 저장하는것
		// int는 속성변수여서 값을 저장하기 때문에 Integer를 넣어줘야 주소를 저장할 수 있다.
		// 아니면 int[]는 배열이고 배열은 객체이기때문에 주소를 가질 수 있다.

		/*
		 * 데이터 int su = 100; A a = new A(); int[]su2 = new int[2];
		 * ================================================ int[]su2 = {1,1}; ==>0번지:
		 * 사람번호, 1번지: 받은 캔디수
		 * 
		 * int[]su2; su2={1, 1}; ==> 에러발생! 선언과 할당을 따로 작성할 수 없음.
		 * ================================================ int[]s2; su2=new
		 * int[]{1,1};=>메모리 할당과 함께 정해진 값을 초기화!
		 * 
		 */
		int no = 1; // 줄서기 번호

		// 첫번째 데이터(사람)입력
		queue.offer(new Person(no, 1)); // ==>0번지: 사람번호, 1번지:받을 캔디수

		Person person;
		int candyTotalCnt = 20; //전체캔디수
		int availableCnt = 0; //받을 캔디수

		while (candyTotalCnt > 0) {
			if (!queue.isEmpty()) { // 대기열에 줄 선 사람이 있다며
				// 캔디 받기(줄에서 나오기)
				person = queue.poll();
				availableCnt = (candyTotalCnt >= person.candycnt) ? person.candycnt : candyTotalCnt;
				candyTotalCnt -= availableCnt; // 캔디를 나눠준만큼 total에서 빼주기

				if (candyTotalCnt == 0) {// 캔디를 전부 나누어 주었을 때
					System.out.println("마지막 캔디를 가져간 사람: " + person.no + "번지");
				} else {// 캔디를 나누어 줄 수 있을때

					System.out.println(">>[" + person.no + "번]캔디" + person.candycnt + "가져가요~");
					person.candycnt++; // 다음의 받을 캔디수 증가
					queue.offer(person);// 다시 줄서기
					queue.offer(new Person(++no, 1));// 다음 사람 줄세우기
				}
			}
		} // while
		
		System.out.println();
		System.out.println("대기열 정보>>>"+queue);
	}// main

}//end class

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
