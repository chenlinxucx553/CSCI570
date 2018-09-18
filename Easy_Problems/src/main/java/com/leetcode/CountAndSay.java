package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
 *
 * @Author: Aaron Yang
 * @Date: 9/18/2018 10:50 AM
 */
public class CountAndSay {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line);

            String ret = new Solution23().countAndSay(n);

            String out = (ret);

            System.out.print(out);
        }
    }
}
class Solution23 {
    public String countAndSay(int n) {
        String code = "1";
        for (int i = 1; i < n; i++) {
            code = readThePrev(code);
        }
        return code;
    }

    private String readThePrev(String code) {
        StringBuffer buffer = new StringBuffer();
        for (int i = 0; i < code.length();){
            int j = 0;
            while(i + j < code.length() &&code.charAt(i) == code.charAt(i + j)) j++;
            buffer.append("" + j + code.charAt(i));
            i += j;
        }
        return buffer.toString();
    }

}
