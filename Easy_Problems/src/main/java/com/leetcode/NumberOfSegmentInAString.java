package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Count the number of segments in a string,
 * where a segment is defined to be a contiguous sequence of non-space characters.
 *
 * @Author: Aaron Yang
 * @Date: 10/17/2018 4:29 PM
 */
public class NumberOfSegmentInAString {
    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String s = stringToString(line);

            int ret = new Solution77().countSegments(s);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }

}

class Solution77 {
    public int countSegments(String s) {
        if ("".equals(s) || "".equals(s.trim())) return 0;
        String[] words = s.trim().split("\\s+");
        return words.length;
    }
}
