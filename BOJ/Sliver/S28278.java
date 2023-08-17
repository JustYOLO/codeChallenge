import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class S28278 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        int[] stack = new int[1_000_000];
        int stackSize = 0;
        for(int i = 0; i < n; i++)
        {
            String[] parts = br.readLine().split(" ");
            int opr = Integer.parseInt(parts[0]);
            if(opr == 1)
            {
                stack[stackSize] = Integer.parseInt(parts[1]);
                stackSize++;
            }
            else if(opr == 2)
            {
                if(stackSize != 0) 
                {
                    sb.append(stack[stackSize-1] + "\n");
                    stackSize--;
                }
                else sb.append("-1\n");
            }
            else if(opr == 3)
            {
                sb.append(stackSize + "\n");
            }
            else if(opr == 4)
            {
                if(stackSize == 0) sb.append("1\n");
                else sb.append("0\n");
            }
            else if(opr == 5)
            {
                if(stackSize != 0) sb.append(stack[stackSize-1] + "\n");
                else sb.append("-1\n");
            }
        }
        System.out.println(sb);
    }
}
