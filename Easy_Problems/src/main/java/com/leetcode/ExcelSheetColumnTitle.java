package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given a positive integer, return its corresponding column title as appear in an Excel sheet.
 *
 * @Author: Aaron Yang
 * @Date: 9/24/2018 8:48 AM
 */
public class ExcelSheetColumnTitle {

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            int n = Integer.parseInt(line);

            String ret = new Solution34().convertToTitle(n);

            String out = (ret);

            System.out.print(out);
        }
    }
}

class Solution34 {

    public String convertToTitle(int n) {
        String res = "";
        while(n != 0) {
            res = (char)('A' + (n - 1) % 26) + res;
            n = (n - 1) / 26;
        }
        return res;
    }
}
