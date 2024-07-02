package algo;

import java.util.Scanner;

public class Main_10988_팰린드롬 {
    public static void main(String[] args) {
        //팰린드롬: 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어
        Scanner sc = new Scanner(System.in);
        String str = sc.nextLine();
        int n= str.length()/2;
        String [] str2 = str.split("");
        int sol =1;
        for(int i=0,j=str.length()-1; i<n; i++,j--){
            if(!(str2[i].equals(str2[j]))){
//                System.out.println(str2[i]+" "+str2[j]);
                sol=0;
                break;
            }
        }
        System.out.println(sol);
    }
}
