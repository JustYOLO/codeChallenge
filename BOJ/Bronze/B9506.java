package BOJ.Bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.System;
import java.util.ArrayList;

public class B9506 {
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = 1;
        ArrayList<Integer> intArr;
        while(true)
        {
            n = Integer.parseInt(br.readLine());
            if(n == -1) break;
            intArr = getDivisor(n);
            if(isPerfect(intArr)) System.out.println(output(intArr));
            else System.out.printf("%d is NOT perfect.\n", n);
        }
        
    }

    public static ArrayList<Integer> getDivisor(int n)
    {
        ArrayList<Integer> intArr = new ArrayList<Integer>();
        for(int i = 1; i <= n; i++)
        {
            if(n % i == 0) intArr.add(i);
        }
        return intArr;
    }

    public static boolean isPerfect(ArrayList<Integer> intArr)
    {
        int sum = 0;
        for(int num: intArr)
        {
            sum += num;
        }
        sum -= intArr.get(intArr.size()-1);
        if(intArr.get(intArr.size()-1) == sum) return true;
        else return false;
    }

    public static String output(ArrayList<Integer> intArr)
    {
        String result = "";
        int target = intArr.get(intArr.size()-1);
        intArr.remove(intArr.size()-1);
        intArr.remove(0);
        result = target + " = 1 ";
        for(int num: intArr)
        {
            result += "+ " + num + " ";
        }
        return result;
    }
}