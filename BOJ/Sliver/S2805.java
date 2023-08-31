import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class S2805
{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] trees = new int[n];
        int max = 0;
        for(int i = 0; i < n; i++)
        {
            trees[i] = Integer.parseInt(st.nextToken());
            if(max < trees[i])
                max = trees[i];
        }

        /*
        max: the highest tree cutter val.
        min: the smallest tree cutter val.
        min val = max tree height - m(target value)
        */
        int min = max - m;
        int mid;
        long sum;
        while(min < max)
        {
            mid = (max + min) / 2;
            sum = 0;
            for(int h: trees)
            {
                if(mid < h)
                    sum += h - mid;
            }
            if(sum < m)
                max = mid;
            else
                min = mid + 1;
        }

        System.out.println(min - 1);
    }
}