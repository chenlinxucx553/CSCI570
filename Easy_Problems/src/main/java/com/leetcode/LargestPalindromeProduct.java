package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Find the largest palindrome made from the product of two n-digit numbers.
 *
 * @Author: Aaron Yang
 * @Date: 10/25/2018 11:56 AM
 */
public class LargestPalindromeProduct {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line);

            int ret = new Solution87().largestPalindrome(n);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution87 {
    public int largestPalindrome(int n) {
        if (1 == n) return 9;
        long maxNumber = (long) (Math.pow(10,n) - 1);
        long minNumber = (long) Math.pow(10, n - 1);

        long maxProduct = maxNumber * maxNumber;
        long start = maxProduct / (long)Math.pow(10, n);

        while (true){
            long candidate = palindrome(start--);
            if(candidate > maxProduct)  continue;
            for(long i = maxNumber; i >= minNumber; i--) {
                if(candidate / i > maxNumber)  break;
                if(candidate % i == 0)  return (int) (candidate % 1337);
            }
        }

    }

    public long palindrome(long num) {
        String str = num + new StringBuilder().append(num).reverse().toString();
        return Long.parseLong(str);
    }
}
