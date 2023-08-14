import java.util.Scanner;

public class S1735 {
public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long[] nums = new long[4];
        int i = 0;
        for(int j = 0; j < 2; j++)
        {
            for(String num: sc.nextLine().split(" "))nums[i++] = Integer.parseInt(num);
        }
        long lcm = getLcm(nums[1], nums[3]);
        nums[0] *= lcm / nums[1];
        nums[2] *= lcm / nums[3];

        nums[0] = nums[0] + nums[2]; nums[1] = lcm;
        nums[3] = euclidean(nums[0], lcm);
        System.out.printf("%d %d\n", nums[0]/nums[3], nums[1]/nums[3]);

        sc.close();
    }
    public static long euclidean(long a, long b)
    {
        if(b == 0) return a;
        return euclidean(b, a % b);
    }
    public static long getLcm(long a, long b)
    {
        return a * b / euclidean(a, b);
    }
}
