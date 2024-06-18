import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Main_BJ_12891_2 {

    static int S;
    static int P;
    static int answer;
    static String DNA;
    static char[] ACGT = {'A', 'C', 'G', 'T'};
    static HashMap<Character, int[]> map = new HashMap<Character, int[]>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        S = Integer.parseInt(st.nextToken());
        P = Integer.parseInt(st.nextToken());
        DNA = br.readLine();
        st = new StringTokenizer(br.readLine());

        // HashMap : (ACGT 문자 하나씩, {현재 카운트, 최소 조건})
        for (char c : ACGT) {
            map.put(c, new int[]{0, Integer.parseInt(st.nextToken())});
        }

        // (일단 세는 부분)1. 입력 받은 DNA 문자열에서 첫 문자 포함하여 P만큼 자른 후 ACGT에 해당하는 문자 세기 2. 조건 만족하는지 체크
        for (int i = 0; i < P; i++) {
            map.get(DNA.charAt(i))[0]++;
        }
        if (isFull()) answer++;

        // (이동하는 부분)인덱스를 1씩 증가시켜가며 슬라이딩 윈도우 적용(오른쪽으로 인덱스 하나씩 이동하여 부분문자열 만듦)
        for (int i = 0; i < S - P; i++) {
            map.get(DNA.charAt(i))[0] -= 1;
            map.get(DNA.charAt(i+P))[0] += 1;
            if (isFull()) answer++;
        }

        System.out.println(answer);

    }

    public static boolean isFull() {
        for (char c : ACGT) {
            if (map.get(c)[0] < map.get(c)[1]) return false;
        }
        return true;
    }
}