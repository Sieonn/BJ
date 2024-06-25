import java.util.Arrays;

public class BinarySearchTest3 {
	/*
	 * Arrays.binarySearch(검색배열, 찾을키값)
	==>이진
	*/
	
	public static void main(String[] args) {
		int [] arr = {1, 2, 3, 5, 6};
		System.out.println(Arrays.binarySearch(arr, 3));//2
		System.out.println(Arrays.binarySearch(arr, 4));//-4 ==>추가할 위치? |-4|-1 ==>3
		
	}//main
}
