package BOJ.Bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B14215 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] len = new int[3];
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        len[0] = Integer.parseInt(st.nextToken());
        len[1] = Integer.parseInt(st.nextToken());
        len[2] = Integer.parseInt(st.nextToken());
        Arrays.sort(len);
        if(len[0] + len[1] > len[2]) System.out.println(len[0] + len[1] + len[2]);
        else System.out.println(len[0]*2 + len[1]*2 - 1);
    }
}
