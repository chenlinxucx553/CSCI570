package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given an integer, write a function to determine if it is a power of two.
 *
 * @Author: Aaron Yang
 * @Date: 10/4/2018 9:23 AM
 */
public class PowerOfTwo {

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line);

            boolean ret = new Solution48().isPowerOfTwo(n);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution48 {
    public boolean isPowerOfTwo(int n) {
        if (n == 0x80000000) return false;  //
        String binaryStr = Integer.toBinaryString(n);
        int count = 0;
        for (char character : binaryStr.toCharArray()) {
            if (character == '1') count++;
            if (count == 2) return false;
        }
        return count == 1;
    }
}
