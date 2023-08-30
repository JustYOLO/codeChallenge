import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class S4779 {
    public static char[] cantor(char[] line)
    {
        if(line.length == 1 || line[1] == ' ') return line;
        else
        {
            int size = 0;
            for(int i = 0; i < line.length; i++)
            {
                if(line[i] == ' ') break;
                else size++;
            }
            size /= 3;
            for(int i = size; i < line.length; i += 2 * size)
            {
                for(int j = i; j < i+size; j++) line[j] = ' ';
            }
        }
        return cantor(line);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        String str;
        int n;
        while((str = br.readLine()) != null)
        {
            n = Integer.parseInt(str);
            char[] line = new char[(int) Math.pow(3, n)];
            for(int i = 0; i < line.length; i++) line[i] = '-';
            sb.append(new String(cantor(line)) + '\n');
        }
        
        System.out.println(sb);
        br.close();
    }
}
