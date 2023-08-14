import java.util.Scanner;

public class S13241 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] nums = new String[2];
        long a, b;
        nums = sc.nextLine().split(" ");
        a = Integer.parseInt(nums[0]);
        b = Integer.parseInt(nums[1]);
        
        System.out.println(a*b/euclidean(a, b));

        sc.close();
    }
    public static long euclidean(long a, long b)
    {
        if(b == 0) return a;
        return euclidean(b, a % b);
    }
}
