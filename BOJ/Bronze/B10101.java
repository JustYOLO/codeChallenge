package BOJ.Bronze;

import java.util.Scanner;

public class B10101 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] angles = new int[3];
        for(int i = 0; i < 3; i++) angles[i] = Integer.parseInt(sc.nextLine());
        if(angles[0] + angles[1] + angles[2] != 180) System.out.println("Error");
        else if(angles[0] == 60 && angles[1] == 60) System.out.println("Equilateral");
        else if(angles[0] == angles[1] || angles[0] == angles[2] || angles[1] == angles[2]) System.out.println("Isosceles");
        else System.out.println("Scalene");

        sc.close();
    }
}
