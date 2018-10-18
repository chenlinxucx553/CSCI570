package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * You have a total of n coins that you want to form in a staircase shape,
 * where every k-th row must have exactly k coins.
 *
 * @Author: Aaron Yang
 * @Date: 10/18/2018 12:41 PM
 */
public class ArrangingCoins {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line);

            int ret = new Solution79().arrangeCoins(n);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution79 {
    public int arrangeCoins(int n) {
        int index = 1;
        while (n >= index) {
            n -= index++;
        }
        return index - 1;
    }
}