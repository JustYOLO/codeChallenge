import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class S17103
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        boolean[] primes = getPrimes();
        for(int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());

            System.out.println(getPartitionNum(num, primes));
        }
    }
    public static boolean[] getPrimes()
    {
        boolean[] num = new boolean[1000001];
        num[0] = num[1] = true;
        for (int i = 2; i * i <= 1000000; i++) {
            if (!num[i]) {
                for (int j = i + i; j <= 1000000; j += i) {
                    num[j] = true;
                }
            }
        }
        return num;
    }
    public static int getPartitionNum(int target, boolean[] primes)
    {
        int ans = 0;
        for(int i = 2; i <= target / 2; i++)
        {
            if(!primes[i] && !primes[target - i]) ans++;
        }
        return ans;
    }
}