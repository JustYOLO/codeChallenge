package BOJ.Bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B9063 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int xMax = -10_000; int yMax = -10_000; int xMin = 10_000; int yMin = 10_000;
        int[] point = new int[2];
        for(int i = 0; i < n; i++)
        {
            point = getPoint(br.readLine().split(" "));
            if(point[0] > xMax) xMax = point[0];
            if(point[0] < xMin) xMin = point[0];
            if(point[1] > yMax) yMax = point[1];
            if(point[1] < yMin) yMin = point[1];
        }
        System.out.println((xMax-xMin)*(yMax-yMin));
    }
    public static int[] getPoint(String[] line)
    {
        int[] intArr = new int[2];
        intArr[0] = Integer.parseInt(line[0]);
        intArr[1] = Integer.parseInt(line[1]);
        return intArr;
    }
}
