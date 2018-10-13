package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
 *
 * @Author: Aaron Yang
 * @Date: 10/13/2018 9:32 AM
 */
public class FirstUniqueCharacterInAString {


    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String s = stringToString(line);

            int ret = new Solution67().firstUniqChar(s);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution67 {
    public int firstUniqChar(String s) {
        int [] map = new int[26];
        int [] index = new int[26];
        char[] characters = s.toCharArray();
        int min = characters.length;
        for (int i = s.length() - 1; i >= 0; i--) {
            map[characters[i] - 'a']++;
            index[characters[i] - 'a'] = i;
        }
        for(int i= 0; i < map.length; i++){
            if(map[i] == 1) min = Math.min(index[i],min);
        }
        return min != characters.length ? min : -1;
    }
}
