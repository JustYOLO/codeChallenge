package BOJ.Bronze;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.System;

public class B2720 {
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] coinArr = {25, 10, 5, 1};
        for(int i = 0; i < n; i++)
        {
            int left = Integer.parseInt(br.readLine());
            for(int coin: coinArr)
            {
                int num = getCoin(coin, left);
                System.out.printf("%d ", num);
                left -= coin*num;
            }
            System.out.println();
        }
        
    }

    public static int getCoin(int coinVal, int left)
    {
        return left/coinVal;
    }

}