import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class S4134 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for(int j = 0; j < n; j++)
        {
            long num = Long.parseLong(br.readLine());
            if(num <= 1)
            {
                System.out.println(2);
                continue;
            }
            while(true)
            {
                if(isPrime(num))
                {
                    System.out.println(num);
                    break;
                }
                else num++;
            }
        }
    }
    public static boolean isPrime(long num)
    {
        long max = (long) Math.sqrt(num);
        for(long i = max; i > 1; i--)
        {
            if(num % i == 0) return false;
        }
        return true;
    }
}
