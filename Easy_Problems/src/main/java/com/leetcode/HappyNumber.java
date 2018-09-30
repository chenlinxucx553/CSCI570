package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

/**
 * Write an algorithm to determine if a number is "happy".
 * <p>
 * A happy number is a number defined by the following process:
 * Starting with any positive integer, replace the number by the sum of the squares of its digits,
 * and repeat the process until the number equals 1 (where it will stay),
 * <p>
 * or it loops endlessly in a cycle which does not include 1.
 * Those numbers for which this process ends in 1 are happy numbers.
 * <p>
 * <p>
 * Example:
 * Input: 19
 * Output: true
 * Explanation:
 * 1^2 + 9^2 = 82
 * 8^2 + 2^2 = 68
 * 6^2 + 8^2 = 100
 * 1^2 + 0^2 + 0^2 = 1
 *
 * @Author: Aaron Yang
 * @Date: 9/30/2018 10:16 AM
 */
public class HappyNumber {


    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line);

            boolean ret = new Solution40().isHappy(n);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution40 {

    public boolean isHappy(int n) {
        Set<Integer> digits = new HashSet<>();
        while (digits.add(n)){
            int sum = 0;
            while(n > 0){
                sum += (n % 10) * (n % 10);
                n /= 10;
            }
            if(sum == 1) return true;
            n = sum;
        }
        return false;
    }

}
