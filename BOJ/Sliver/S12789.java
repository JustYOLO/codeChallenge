import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class S12789
{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Stack<Integer> currentLine = new Stack<>();
        Stack<Integer> leftLine = new Stack<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] nums = new int[n];
        for(int i = 0; i < n; i++) nums[i] = Integer.parseInt(st.nextToken());
        for(int i = n-1; i >= 0; i--) currentLine.add(nums[i]);

        int target = 1;
        while(currentLine.size() + leftLine.size() != 0)
        {
            if(currentLine.contains(target))
            {
                int tmp;
                while(true)
                {
                    tmp = currentLine.pop();
                    if(tmp == target) break;
                    else leftLine.add(tmp);
                }
            }
            else
            {
                if(target != leftLine.pop())
                {
                    System.out.println("Sad");
                    System.exit(0);
                }
            }
            target++;
        }
        System.out.println("Nice");
        br.close();
    }
}