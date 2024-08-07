import java.util.Scanner;

public class Main_BJ_16926_배열돌리기1 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    StringBuilder sb = new StringBuilder();
    
    int n = sc.nextInt();
    int m = sc.nextInt();
    int r = sc.nextInt();
    int arr[][] = new int[n][m];
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};
    int t = Math.min(n, m) / 2;

    for(int i = 0; i < n; i++) {
      for(int j = 0; j < m; j++) arr[i][j] = sc.nextInt();
    }

    for(int k = 0; k < r; k++) {
      for(int i = 0; i < t; i++) {
        int a = i;
        int b = i;
        int tmp = arr[i][i];
        int j = 0;
        
        while(j < 4) {
          int x = a + dx[j];
          int y = b + dy[j];
          if(x >= i && x < n - i && y >= i && y < m - i) {  // 각 모서리
            arr[a][b] = arr[x][y];
            a = x;
            b = y;
          }
          else j++;
        }
        arr[i + 1][i] = tmp;
      }
    }

    for(int i = 0; i < n; i++) {
      for(int j = 0; j < m; j++) sb.append(arr[i][j]+" ");
      sb.append("\n");
    }
    
    System.out.print(sb);
  }
}