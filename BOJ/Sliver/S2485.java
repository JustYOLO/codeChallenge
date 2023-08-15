import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;

public class S2485 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashSet<Integer> distanceSet = new HashSet<>();

        int n = Integer.parseInt(br.readLine());
        int[] trees = new int[n];
        for(int i = 0; i < n; i++) 
        {
            trees[i] = Integer.parseInt(br.readLine());
            if(i >= 1) distanceSet.add(trees[i] - trees[i-1]);
        }

        int gcd;
        if(distanceSet.contains(1)) gcd = 1;
        else gcd = getListGCD(distanceSet);

        System.out.println((trees[n-1] - trees[0]) / gcd - trees.length + 1);
    }
    public static int getListGCD(HashSet<Integer> numSet)
    {
        int[] nums = new int[numSet.size()];
        int i = 0;
        for(int num: numSet) nums[i++] = num;
        Arrays.sort(nums);
        for(i = 0; i < nums.length - 1; i++) nums[i+1] = euclidean(nums[i], nums[i+1]);
        return nums[nums.length - 1];
    }
    public static int euclidean(int a, int b)
    {
        if(b == 0) return a;
        return euclidean(b, a % b);
    }
}