package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given two binary strings, return their sum (also a binary string).
 *
 * @Author: Aaron Yang
 * @Date: 9/14/2018 10:42 AM
 */
public class AddBinary {

    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String a = stringToString(line);
            line = in.readLine();
            String b = stringToString(line);

            String ret = new Solution13().addBinary(a, b);

            String out = (ret);

            System.out.print(out);
        }
    }
}

class Solution13 {
    public String addBinary(String a, String b) {
        int carry = 0;
        int sum = 0;
        int ascii_a = 0;
        int ascii_b = 0;
        StringBuilder result = new StringBuilder();
        while (a.length() != b.length()) {
            if (a.length() > b.length()) {
                b = "0" + b;
            } else {
                a = "0" + a;
            }
        }
        for (int i = a.length() - 1; i >= 0; i--) {
            ascii_a = a.charAt(i) - '0';    //ASCII 做加減 CHAR->INT
            ascii_b = b.charAt(i) - '0';
            sum = ascii_a + ascii_b + carry;
            if (sum >= 2) {
                result.append((char) (sum - 2 + '0'));  // INT -> CHAR
                carry = 1;
            } else {
                result.append((char) (sum + '0'));
                carry = 0;
            }

        }
        if (carry == 1) {
            result.append("1");
        }
        return result.reverse().toString();
    }
}
