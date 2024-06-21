package day0621;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class PrintSpeedTest {

	public static void main(String[] args)throws Exception {
		BufferedWriter bw =  new BufferedWriter(new OutputStreamWriter(System.out));
//		bw.append('a');
//		bw.write("");

		// String고정문자열 StringBuilder 가변문자열

		StringBuilder sb = new StringBuilder();

		long start = System.currentTimeMillis();
//		long start = System.nanoTime();
		for (int i = 0; i < 1000; i++) {
//			System.out.println("유레카!");
//			sb.append("유레카~!!\n");

//			sb.append("유레카~!!");
//			sb.append("\n");

			sb.append("유레카!").append('\n');
		}//for문 
		
		long end = System.currentTimeMillis();
//		long end = System.nanoTime();

		System.out.println("출력시간:" + (end - start));
		
		bw.close();
	}// main

}
