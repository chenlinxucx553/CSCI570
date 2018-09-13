package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
 * return the length of last word in the string.  If the last word does not exist, return 0.
 *
 * @Author: Aaron Yang
 * @Date: 9/13/2018 10:40 AM
 */
public class LengthofLastWord {
    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String s = stringToString(line);

            int ret = new Solution11().lengthOfLastWord(s);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution11 {
    public int lengthOfLastWord(String s) {
        String[] words = s.split("\\s+");
        //If the last word does not exist, return 0.
        if(words.length == 0){
            return 0;
        }
        return words[words.length - 1].length();
    }
}
