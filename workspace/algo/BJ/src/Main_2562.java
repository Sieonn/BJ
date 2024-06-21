import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main_2562 {

	public static void main(String[] args)throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int [] nums= new int [9];
		int [] nums2 = new int[9];
		for(int i = 0; i<9; i++) {
			nums[i] = Integer.parseInt(br.readLine());
			nums2[i] = nums[i];
		}
		Arrays.sort(nums);
		int maxidx = 0;
		for(int i =0; i<9; i++) {
			if(nums2[i]==nums[8]) {
				maxidx = i;
			}
		}
//		System.out.println(Arrays.toString(nums)+maxidx);
		System.out.println(nums[8]+"\n" + (maxidx+1));
	}

}
