import java.util.ArrayDeque;
import java.util.Queue;

public class QueueTest {

	public static void main(String[] args) {
		Queue<String> queue = new ArrayDeque<String>();
		System.out.println("큐의 요소 개수:"+queue.size()+", 큐Empty체크:"+queue.isEmpty());
		queue.offer("홍길동");
		queue.offer("길라임");
		queue.offer("김주원");
	}

}
