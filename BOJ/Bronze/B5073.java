package BOJ.Bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class B5073 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] len = new int[3];
        while(true)
        {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            len[0] = Integer.parseInt(st.nextToken());
            len[1] = Integer.parseInt(st.nextToken());
            len[2] = Integer.parseInt(st.nextToken());
            if(len[0] == 0) break;
            Arrays.sort(len);
            output(check(len));
        }
    }

    public static int check(int[] len)
    {
        if(len[0] + len[1] <= len[2]) return 1;
        else if(len[0] == len[1] && len[1] == len[2]) return 2;
        else if(len[0] == len[1] || len[1] == len[2] || len[0] == len[2]) return 3;
        else return 4;
    }
    public static void output(int n)
    {
        if(n == 1) System.out.println("Invalid");
        else if(n == 2) System.out.println("Equilateral");
        else if(n == 3) System.out.println("Isosceles");
        else System.out.println("Scalene");
    }
}
