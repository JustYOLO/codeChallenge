import java.util.Scanner;

public class Nqueen {
    static int count = 0;
    public static void search(int i, int[] col) {
        int n = col.length - 1;
        if(promising(i, col)) {
            if(i == n) count++;
            else {
                for(int j = 1; j <= n; j++) {
                    col[i+1] = j;
                    search(i+1, col);
                }
            }
        }
    }
    public static boolean promising(int i, int[] col) {
        int k = 1;
        boolean flag = true;
        while(k < i) {
            if(col[i] == col[k] || Math.abs(col[i] - col[k]) == (i - k)) {
                flag = false;
                break;
            }
            k++;
        }
        return flag;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        int[] col = new int[n+1];
        for(int i = 0; i < n+1; i++) col[i] = 0;
        search(0, col);
        System.out.println(count);
    }
}
