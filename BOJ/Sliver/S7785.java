import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.StringTokenizer;

public class S7785 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        HashSet<String> employeeSet = new HashSet<>();
        for(int i = 0; i < n; i++)
        {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            if(isEnter(st.nextToken())) employeeSet.add(name);
            else employeeSet.remove(name);
        }
        String[] sorted = new String[employeeSet.size()];
        int i = 0;
        for(String element: employeeSet) sorted[i++] = element;
        Arrays.sort(sorted, Comparator.reverseOrder());
        for(String employee: sorted) System.out.println(employee);

        br.close();
    }
    public static boolean isEnter(String status)
    {
        if(status.equals("enter")) return true;
        else return false;
    }
}