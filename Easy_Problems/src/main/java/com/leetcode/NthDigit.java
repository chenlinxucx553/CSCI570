package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
 *
 * @Author: Aaron Yang
 * @Date: 10/14/2018 9:49 AM
 */
public class NthDigit {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line);

            int ret = new Solution69().findNthDigit(n);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution69 {
    public int findNthDigit(int n) {

        int digitLength = 1;
        int startNumber = 1;
        long numberCount = 9;
        while (n > digitLength * numberCount) {
            n -= digitLength * numberCount;
            digitLength++;
            numberCount *= 10;
            startNumber *= 10;
        }

        startNumber += (n - 1) / digitLength;
        String s = Integer.toString(startNumber);
        return Character.getNumericValue(s.charAt((n - 1) % digitLength));
    }
}

