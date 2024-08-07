package algo;

import java.util.Scanner;

public class Main_2603_색종이 {
	static int [][] spaces;
	static int blue=0;
	static int white=0;
	public static void main(String[] args) {
		 Scanner sc= new Scanner(System.in);
		 int N = sc.nextInt(); //전체종이의 한 변의 길이
		 spaces = new int[N][N];
		 
		 
		 //데이터 입력
		for(int i=0; i<N;i++) {
			for(int j=0; j<N; j++) {
				spaces[i][j]= sc.nextInt();
			}
		}
		recursiveCut(0,0,N); //시작 행인덱스, 시작 열인덱스, 한변의 길이
		
		System.out.println(white);
		System.out.println(blue);
		 
		 sc.close();
		 //main
	}
	private static void recursiveCut(int rowIdx, int colIdx, int length) {

		int sum=0;
		
		for(int i=rowIdx; i<rowIdx+length; i++) {//행인덱스
			for(int j =colIdx; i<colIdx+length; j++) {//열인덱스
				sum+=spaces[i][j];
			}
			
		}
		if(sum==length*length) {//전체 파란색 색종이
			blue++;
		}else if(sum==0){//전체 하얀색 색종이
			white++;
		}else {
			
		}
		
		int newLength = length/2;
		//4등분된 영역에 대해 재귀호출 ==> 서로 일치하지 않는 색을 만났을 때
		recursiveCut(rowIdx, colIdx, newLength);	//좌상
		recursiveCut(rowIdx, colIdx+newLength, newLength);	//우상
		recursiveCut(rowIdx+newLength, colIdx, newLength);	//좌하
		recursiveCut(rowIdx+newLength, colIdx+newLength, newLength);	//우하
		
	}//recursiveCut
}
