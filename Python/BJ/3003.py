chess = [1,1,2,2,2,8]
n = list(map(int, input().split()))
result=[]
for i in range(len(n)):
    val = chess[i] - n[i]
    result.append(val)
print(*result)

# import java.util.Arrays;
# import java.util.Scanner;

# public class Main {

# 	public static void main(String[] args) {
# 		//킹:1, 퀸:1, 룩:2, 비숍:2, 나이트:2, 폰:8
# 		//검정은 있는데 흰색이 수가 이상함
# 		Scanner sc =  new Scanner(System.in);
# 		int [] sol = {1,1,2,2,2,8};
# 		String str = sc.nextLine();
# 		String [] sarr = new String[sol.length];
# 		sarr=str.split(" ");
# 		int [] sol2 = new int [sarr.length];
# 		for(int i=0; i<sarr.length; i++) {
# 			sol2[i]+=sol[i]-Integer.parseInt(sarr[i]);
			
# 			System.out.print(sol2[i]+" ");
# 		}
# 	}

# }