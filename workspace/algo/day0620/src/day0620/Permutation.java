package day0620;

import java.util.Arrays;

public class Permutation {

	static int N, totalCount;  //N선택할 수 있는 요소의 전체개수
	static int[] numbers = {3,5,7};
	static boolean[] selected; //selected가 있으면 중복된 것은 안나온다.
	static int[] ans;//뽑아진 데이터를 저장할 곳
	
	public static void main(String[] args) {
		N = numbers.length;
		ans = new int[N];
		selected = new boolean[N];
		go(0);
		System.out.println("===> "+totalCount);
	}

	private static void go(int count) {
		if(count == N) { //count 몇개 뽑았는지 횟수 N은 전체를 다 뽑겠다 라는것을 의미
			totalCount++;
			System.out.println(Arrays.toString(ans));
			return;
		}
		for (int i = 0; i < N; i++) {
			if(!selected[i]) {
				selected[i] = true;
				ans[count] = numbers[i];
				go(count+1);
				selected[i] = false;
			}
		}
		
	}

}
