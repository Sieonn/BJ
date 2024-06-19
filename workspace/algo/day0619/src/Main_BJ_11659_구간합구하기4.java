//import java.util.Scanner;
//
//public class Main_BJ_11659_구간합구하기4 {
//
//	public static void main(String[] args) {
//		Scanner sc= new Scanner(System.in);
//		String [] num = sc.nextLine().split(" ");
//		String [] arr = sc.nextLine().split(" ");
//		String [] index = sc.nextLine().split(" ");
//		int start = Integer.parseInt(index[0]);
//		int end = Integer.parseInt(index[1]);
//		
//		int sum=0;
//		for(int i=start-1; i<end; i++) {
//			sum+=Integer.parseInt(arr[i]);
//		}
//		System.out.println(sum);
//	}
//
//}
// 같을 배열을 두고 구간을 여러번 지정해주는 경우여서 런타임 에러가 생기는것


import java.util.*;

public class Main_BJ_11659_구간합구하기4 {
 
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N, M;
        
        N = sc.nextInt();
        M = sc.nextInt();
        
        int[] arr = new int[N+1];
        
        for(int i=1; i<=N; i++) {
            arr[i] = arr[i-1] + sc.nextInt();
            
        }
        
        int a, b; // 시작항과 끝항
        for(int i=0; i<M; i++) {
            a = sc.nextInt();
            b = sc.nextInt();
            
            System.out.println(arr[b]-arr[a-1]);
        }
        
    }
}