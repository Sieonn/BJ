import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main_2798_블랙젝 {

	public static void main(String[] args)throws Exception {
		//3장을 뽑아서 카드의 합이 M을 넘지 않으면서 카드의 합을 최대한 크게 만드는 게임
		//N카드 갯수 M:최대합
		//5장의 카드 목록
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		int N = Integer.parseInt(st.nextToken()); //카드 갯수
		int M = Integer.parseInt(st.nextToken()); //합해서 나올 수 있는 최대 값
		
		StringTokenizer st1 = new StringTokenizer(br.readLine()," ");
		//카드 배열
		int [] cards  = new int[N];
		for(int i =0; i<N; i++) {
			cards[i] = Integer.parseInt(st1.nextToken());
		}
		
		ArrayList<Integer> list = new ArrayList<>();
//		int sum=0;
		for(int i=0; i<N; i++) {
			for(int j=i+1; j<N; j++) {
				for(int k=j+1; k<N; k++) {
					int sum=0;
					sum+=cards[i]+cards[j]+cards[k];
					if(0<=M-sum) {
						list.add(M-sum);		
					}
				}
			}
		}//for
		Collections.sort(list);
		System.out.println(M-(list.get(0)));
	}

}
