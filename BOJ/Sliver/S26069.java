import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class S26069 
{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Set<String> dancing = new HashSet<>();
        dancing.add("ChongChong");
        int n;
        n = Integer.parseInt(br.readLine());
        String names[] = new String[2];
        for(int i = 0; i < n; i++)
        {
            names = br.readLine().split(" ");
            if(dancing.contains(names[0]))
            {
                dancing.add(names[1]);
            }
            else if(dancing.contains(names[1]))
            {
                dancing.add(names[0]);
            }
        }
        System.out.println(dancing.size());
    }
}