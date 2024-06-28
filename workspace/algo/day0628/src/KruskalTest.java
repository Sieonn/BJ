import java.util.Arrays;
import java.util.Scanner;

public class KruskalTest {
	static class Edge implements Comparable<Edge>{// 두 정점과 가중치를 저장
		int start;
		int end;
		int weight; //가중치

		public Edge(int start, int end, int weight) {
			super();
			this.start = start;
			this.end = end;
			this.weight = weight;
		}

		@Override
		public String toString() {
			return "Edge [start=" + start + ", end=" + end + ", weight=" + weight + "]";
		}

		@Override
		public int compareTo(Edge o) {
			
			return this.weight -o.weight;
		}


		

	}

	static int V;
	static int E;
	static int[] parents;
	static Edge[] edgeList;

	public static void main(String[] args) {
		// 입력값(첫행): 노드수, 간선수
		// 입력값(두번째 행 이후): 노드1, 노드2, 가중치

		// 출력값: 최소 스패닝트리를 구성하고 그 트리의 가중치 합을 구하시오.
		Scanner scan = new Scanner(System.in);
		V = scan.nextInt(); // 정점(노드)
		E = scan.nextInt(); // 간선수

		parents = new int[V]; // 부모(대표자)인덱스 저장 배열
		edgeList = new Edge[E]; // 간선 정보 저장 배열

		// 데이터입력
		for (int i = 0; i < E; i++) {
			edgeList[i] = new Edge(scan.nextInt(), scan.nextInt(), scan.nextInt());

		}

		// 각 노드(정점)의 집합만들기
		make();
		
		//최소신장트리의 가중치의 합구하기!
//		Arrays.sort(edgeList); //간선 오름차순
		
		int sum =0;
		int cnt = 0; //찾은 조건을 만족하는 간선의 수
		for( Edge edge : edgeList) {
			if(union(edge.start,edge.end)){ //사이클이 발생하지 않는다면
			sum+= edge.weight;
			
			if(++cnt == V-1)break; //최소신장트리를 만족하는 간선을 전부 찾았다면=> 정점수-1
		}
		}
		
		scan.close(); // 알고리즘은 close하는데 시간이 걸리기 때문에 굳이 안해도됨
	}// main

	static void make() { // 각 집합 생성
		for (int i = 0; i < V; i++) {
			parents[i] = i;

		}
	}// make

	static int find(int a) {// 대표자 찾기
		if (parents[a] == a)
			return a; // 대표자 찾음
		return find(parents[a]);// 부모인덱스의 대표자를 찾아 주세요.
	}// find

	static boolean union(int a, int b) {// 집합 합치기(대표자 일치시키기)
		int aRoot = find(a);
		int bRoot = find(b);
		if (aRoot == bRoot)
			return false;

		//==합치기 작업==
		parents[bRoot] = aRoot; // a그룹의 대표자를 전체(b그룹의) 대표자로 하겠다.
		return true;
	}//union

}
