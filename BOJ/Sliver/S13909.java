import java.util.Scanner;

public class S13909 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = Integer.parseInt(sc.nextLine());
        int ans = 0;
        for(int i = 1; i <= Math.sqrt(num); i++) if(i*i <= num) ans++;
        System.out.println(ans);
        sc.close();
    }
}
