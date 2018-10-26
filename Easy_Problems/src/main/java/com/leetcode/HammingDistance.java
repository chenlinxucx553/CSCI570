package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * The Hamming distance between two integers is the number of positions
 * at which the corresponding bits are different.
 *
 * @Author: Aaron Yang
 * @Date: 10/21/2018 9:36 AM
 */
public class HammingDistance {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int x = Integer.parseInt(line);
            line = in.readLine();
            int y = Integer.parseInt(line);

            int ret = new Solution83().hammingDistance(x, y);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution83 {
    public int hammingDistance(int x, int y) {
        return Integer.bitCount(x ^ y);
    }
}
