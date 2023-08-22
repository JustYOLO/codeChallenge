import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
// used int array to implement deque, but time exceeded.
// update1: if not using move function (starts the array in 0), execution time does not exceeded. 
public class S28279
{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());
        Deque<Integer> d = new ArrayDeque<>();
        int opr;
        for(int i = 0; i < n; i++)
        {
            String[] parts = br.readLine().split(" ");
            opr = Integer.parseInt(parts[0]);
            if(opr == 1) d.addFirst(Integer.parseInt(parts[1]));
            else if(opr == 2) d.addLast(Integer.parseInt(parts[1]));
            else if(opr == 3)
            {
                if(d.size() == 0) sb.append("-1\n");
                else sb.append(d.pollFirst() + "\n");
            }
            else if(opr == 4)
            {
                if(d.size() == 0) sb.append("-1\n");
                else sb.append(d.pollLast() + "\n");
            }
            else if(opr == 5) sb.append(d.size() + "\n");
            else if(opr == 6)
            {
                if(d.size() == 0) sb.append("1\n");
                else sb.append("0\n");
            }
            else if(opr == 7)
            {
                if(d.size() == 0) sb.append("-1\n");
                else sb.append(d.getFirst() + "\n");
            }
            else if(opr == 8)
            {
                if(d.size() == 0) sb.append("-1\n");
                else sb.append(d.getLast() + "\n");
            }
        }
        System.out.println(sb);
    }
}
