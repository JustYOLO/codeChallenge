import java.util.Scanner;
import java.util.StringTokenizer;

public class B19532 {
    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        StringTokenizer st = new StringTokenizer(sc.nextLine(), " ");
        int[] n = new int[6];
        for(int i = 0; i < 6; i++)
        {
            n[i] = Integer.parseInt(st.nextToken());
        }
        int x = 0, y = 0;
        outerLoop :
        for(int a = -999; a <= 999; a++)
        {
            for(int b = -999; b <= 999; b++)
            {
                if(n[0]*a + n[1]*b == n[2] && n[3]*a + n[4]*b == n[5]) 
                {
                    x = a; y = b;
                    break outerLoop;
                }
            }
        }
        System.out.printf("%d %d\n", x, y);
    }
}