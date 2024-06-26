import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main_5622_다이얼 {

	public static void main(String[] args)throws Exception {
		//숫자 1을 입력하려면 2초
		//+1 할 때마다 +1초
		Map<String, Integer> maps = new HashMap<>(); 
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		String [] arr = str.split("");
 		maps.put("A", 3);
		maps.put("B", 3);
		maps.put("C", 3);
		maps.put("D", 4);
		maps.put("E", 4);
		maps.put("F", 4);
		maps.put("G", 5);
		maps.put("H", 5);
		maps.put("I", 5);
		maps.put("J", 6);
		maps.put("K", 6);
		maps.put("L", 6);
		maps.put("M", 7);
		maps.put("N", 7);
		maps.put("O", 7);
		maps.put("P", 8);
		maps.put("Q", 8);
		maps.put("R", 8);
		maps.put("S", 8);
		maps.put("T", 9);
		maps.put("U", 9);
		maps.put("V", 9);
		maps.put("W", 10);
		maps.put("X", 10);
		maps.put("Y", 10);
		maps.put("Z", 10);
		
		int sum=0;
		for(int i=0; i<str.length(); i++) {
			sum+=maps.get(arr[i]);
		}
		System.out.println(sum);
	}

}
