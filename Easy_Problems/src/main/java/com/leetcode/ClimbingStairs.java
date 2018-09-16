package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * You are climbing a stair case. It takes n steps to reach to the top.
 *
 * @Author: Aaron Yang
 * @Date: 9/15/2018 1:44 PM
 */
public class ClimbingStairs {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line);

            int ret = new Solution15().climbStairs(n);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution15 {
    public int climbStairs(int n) {

        if(n == 1) return 1;
        int[] result = new int[n];
        for (int i = 0; i < result.length; i++){
            result[i] = -1;
        }
        result[0] = 1;
        result[1] = 2;
        return dp(n - 1, result);

    }

    private int dp(int n, int[] result) {
        if(result[n] == -1){
            result[n] = dp(n - 1, result) + dp(n - 2,result);
        }
        return result[n];
    }
}
