import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main
{
    private int[] deque;
    private int length;
    private int starts;
    public Main()
    {
        deque = new int[2_000_000];
        length = 0;
        starts = 1_000_000;
    }
    public void f1(int n)
    {
        deque[--starts] = n;
        length++;
    }
    public void f2(int n)
    {
        deque[starts + length] = n;
        length++;
    }
    public int f3()
    {
        if(length == 0) return -1;
        else
        {
            length--;
            return deque[starts++];
        }
    }
    public int f4()
    {
        if(length == 0) return -1;
        else
        {
            length--;
            return deque[starts + length];
        }
    }
    public int f5() { return length; }
    public int f6()
    {
        if(length == 0) return 1;
        else return 0;
    }
    public int f7()
    {
        if(length == 0) return -1;
        else return deque[starts];
    }
    public int f8()
    {
        if(length == 0) return -1;
        else return deque[starts + length - 1];
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Main d = new Main();
        int n = Integer.parseInt(br.readLine());
        int opr;
        for(int i = 0; i < n; i++)
        {
            String[] parts = br.readLine().split(" ");
            opr = Integer.parseInt(parts[0]);
            if(opr == 1) d.f1(Integer.parseInt(parts[1]));
            else if(opr == 2) d.f2(Integer.parseInt(parts[1]));
            else if(opr == 3) sb.append(d.f3() + "\n");
            else if(opr == 4) sb.append(d.f4() + "\n");
            else if(opr == 5) sb.append(d.f5() + "\n");
            else if(opr == 6) sb.append(d.f6() + "\n");
            else if(opr == 7) sb.append(d.f7() + "\n");
            else if(opr == 8) sb.append(d.f8() + "\n");
        }
        System.out.println(sb);
    }    
}