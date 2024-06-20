package day0620;

public class RecursiveTest {
	static int arr[] = { 10, 20, 30 };

	private static void printArray1() {
		for (int i = 0; i < arr.length; ++i) {// 반복조건 => 기본파트
			System.out.print(arr[i] + "\t");// 실행문장(서비스 핵심 코드, 알고리즘 코드) ==>유도파트
		}
	}

	// 재귀함수(자신의 메서드를 다시 호출)
	private static void recursive(int i) {// printArray2() int i =0;
		if (i >= arr.length)return; // 기저조건(끝나는 조건)

		System.out.print(arr[i] + "\t"); // 유도 파트
//		recursive(++i);==> i=i+1
		recursive(i+1);

	}

	public static void main(String[] args) {
		printArray1();
		System.out.println("\n========================");
		recursive(0);
	}

}