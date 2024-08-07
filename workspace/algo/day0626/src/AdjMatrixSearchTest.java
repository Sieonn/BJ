import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class AdjMatrixSearchTest {

	static int N;
	static boolean adjMatrix[][];

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt(); // 정점수
		int C = sc.nextInt(); // 간선수

		adjMatrix = new boolean[N][N];
		for (int i = 0; i < C; ++i) {
			int from = sc.nextInt();
			int to = sc.nextInt();
			adjMatrix[to][from] = adjMatrix[from][to] = true;
		}

		System.out.println("=========bfs1(너비우선탐색)===========");
		bfs1();

		sc.close();
	}// main

	//큐에서 나갈때 방문처리
	private static void bfs1() {
		// 1.큐생성
//		Queue<Integer> queue = new LinkedList<>();
		Queue<Integer> queue = new ArrayDeque<>();
		boolean visited[] = new boolean[N];

		// 2.시작정점 추가
		int current = 0; // 시작정점(인덱스)을 표현
		queue.offer(current);

		// 3.대기열의 정점 방문(탐색) ==> 언제까지? ==> 큐가 빈상태일때까지!!
		while (!queue.isEmpty()) {// 한개 이상의 정점정보가 존재한다면
			current = queue.poll(); // 가장 먼저 입력된 정점을 얻어오기
			
			//>>>>>>>>>>>>>>>>>>>>>>> 중복 추가 발생 방지
			if (visited[current]) {
				System.err.println("이미 처리된 정점입니다.");
				continue;
			}
			// 4. 방문처리
			visited[current] = true; // 방문(처리)된 것을 체크
			System.out.println((char) (current + 'A'));
			// 5.자식정점(인접정점)찾기
			for (int i = 0; i < N; i++) {// 인접한 노드들!! ==> 큐에 입력!!
				if (!visited[i] && adjMatrix[current][i]) {// 현재 노드에 인접하였다면
					queue.offer(i);
				}
			}
		} // while
	}// bfs1
}// end class
