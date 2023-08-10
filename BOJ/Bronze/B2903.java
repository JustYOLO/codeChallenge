package BOJ.Bronze;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.System;

public class B2903 {
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int lines = 2;
        for(int i = 0; i < n; i++)
        {
            lines = 2*lines - 1;
        }
        System.out.println(lines*lines);
    }
}