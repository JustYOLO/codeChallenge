import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class S2805
{
    public static int binarySearch(int[] trees, int a, int b, int target)
    {
        int mid = (a + b) / 2;
        int result = getHeight(trees, mid);
        if(result > target) return binarySearch(trees, mid, b, target);
        else if(result < target) return binarySearch(trees, a, mid, target);
        else return mid;
    }
    public static int getHeight(int[] trees, int mid)
    {
        int sum = 0;
        for(int h: trees)
            if(mid < h) sum += h - mid;
        return sum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] trees = new int[n];
        for(int i = 0; i < n; i++)
        {
            trees[i] = Integer.parseInt(st.nextToken());
        }

        /*
        max: the highest tree cutter val.
        min: the smallest tree cutter val.
        min val = max tree height - m(target value)
        */

        int max = 0;
        for(int i: trees)
            max = Math.max(i, max);
        int min = max - m;

        System.out.println(binarySearch(trees, min, max, m));
    }
}