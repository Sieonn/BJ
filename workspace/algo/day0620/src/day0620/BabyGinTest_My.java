package day0620;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class BabyGinTest_My {

	static int N = 6; // 요소의 개수 고정되어 있다면 =6해놔도 됨
	
	static int[] numbers; // 실행 중 입력
	static int[] ans;// 생성된 순열을 저장

	static boolean[] selected; // 뽑은 수는 다시 뽑지 않음 => 중복제거

	public static void main(String[] args) throws Exception {
		System.setIn(new FileInputStream("babygin.txt"));
		Scanner scan= new Scanner(System.in);
		int T = scan.nextInt();
//		N = numbers.length;
//		N =6;//Baby-Gin의 전체수 길이

		ans = new int[N];
		numbers = new int[N];
		
		selected = new boolean[N];
		
		//"667767"==>문자열 String ==>{'6','6', '7', '7', '6', '7'}
		//=> {6, 6, 7, 7, 6, 7}
		char[]data = scan.next().toCharArray();
		
		//'6'==54 '6'-48:6 '6'-0:6
		for(int i=0; i<N; i++) {
			numbers[i]=data[i]-'0';
		}

		
		boolean flag  = go(0);
		if(flag)
			System.out.println("Baby-Gin");
		else
			System.out.println("Not Baby-Gin");

	}//테스트 케이스 for

	// 연속된 3개의 수 검사! ex) 3 4 5
	static boolean run(int[] cards) {
//		if(cards[2]== cards[1]+1 && cards[1] == cards[0]+1) return true;
		return cards[2] == cards[1] + 1 && cards[1] == cards[0] + 1;
	}

	// 동일한 3개의 수 검사! ex) 3 3 3
	static boolean tri(int[] cards) {
//		if(cards[2]== cards[1]+1 && cards[1] == cards[0]+1) return true;
		return cards[2] == cards[1]  && cards[1] == cards[0];
	}
	
	static boolean isBabyGin() {
		int [] leftCards = new int [] {ans[0],ans[1], ans[2]}; //좌측 카드
		int [] rightCards = new int [] {ans[3],ans[4], ans[5]}; //우측 카드
		
		return (run(leftCards) || tri(leftCards)) && (run(rightCards) || tri(rightCards));
	}
	//순열을 뽑는 함수
	private static boolean go(int count) {
		if (count == N) { // 순열의 조합이 끝났다면
//			isBabyGin();
//			return;
			if(isBabyGin()) return true;
		}

		for (int i = 0; i < N; i++) {
			if (!selected[i]) {
				selected[i] = true; // 선택체크
				ans[count] = numbers[i];
				if(go(count + 1)) return true;
				selected[i] = false;// 선택체크
			}
		}
		return false;
	}

}
