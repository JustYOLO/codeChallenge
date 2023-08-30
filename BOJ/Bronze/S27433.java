import java.util.Scanner;

public class S27433
{
    public static long factorial(int n)
    {
        if(n == 0 || n == 1) return 1;
        else
        {
            return n * factorial(n-1);
        }
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(factorial(Integer.parseInt(sc.nextLine())));
    }
}