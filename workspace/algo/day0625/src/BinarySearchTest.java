import java.util.Arrays;

public class BinarySearchTest {
	private static int[] values= {3, 11, 15, 20, 21, 29, 45, 59, 65, 72};	
	//                            0   1   2   3  4    5   6  7    8  9
	
	
	public static void main(String[] args) {
		System.out.println(binarySearch(65));
		System.out.println(binarySearch(3));
		System.out.println(binarySearch(2));
		System.out.println(binarySearch(46));
		System.out.println(binarySearch(72));
		System.out.println("========================");
		System.out.println(binarySearch2(65,0, values.length-1));
		System.out.println(binarySearch2(3,0,values.length-1));
		System.out.println(binarySearch2(2,0,values.length-1));
		System.out.println(binarySearch2(46,0,values.length-1));
		System.out.println(binarySearch2(72,0,values.length-1));
		System.out.println("========================");
		System.out.println(Arrays.binarySearch(values, 65));
        System.out.println(Arrays.binarySearch(values, 3));
        System.out.println(Arrays.binarySearch(values, 2));
        System.out.println(Arrays.binarySearch(values, 46));
        System.out.println(Arrays.binarySearch(values, 72));
	}//main
	
	
//			start=end=mid=0;
//		System.out.println(mid);
//		System.out.println(end);
	
	
	private static int binarySearch(int key) { //key: 찾고자 하는 값
	//클래스에 선언된 애들은 명시적으로 0이라고 초기화해주지 않아도 0으로 초기화 되는데 얘네는 아님
		int start=0,end=values.length-1,mid =0;//지역변수는 반드시 초기화해서 사용
		//=>시작인덱스,끝인덱스,중앙인덱스
		
		while(start<=end) {//검색할 수 있는 조건
			mid = (start+end)/2;
			
			if(values[mid]==key) {//key값을 찾았다면 종료
				return mid;//찾은 인덱스 리턴
			}
			else if(values[mid]<key)//start증가 (찾고자 하는 값이 mid보다 컸을때)
				start = mid+1;
			else //if(values[mid] >key
				end = mid-1;//end 감소(찾고자 하는 값이 mid보다 적었을 때)
		}//while
		return -1;//찾지 못했음 리턴
	}
	private static int binarySearch2(int key, int start, int end) {
		if(start<=end) {
			int mid = (start+end)/2;
			if(values[mid] ==key)return mid;
			else if(values[mid]<key)  //start증가 (찾고자하는 값이mid보다 컸을때)
				//start = mid+1;
				return binarySearch2(key,mid+1,end);
			else //end =mid-1; // end감소( 찾고자하는 값이 mid보다 적었을때)
				return binarySearch2(key,start, mid-1);
		}
		return -1;
	}//binarySearch2

}//반복문
