package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class LongestCommonPrefix {

    public static String[] stringToStringArray(String input) {
        JsonArray jsonArray = JsonArray.readFrom(input);
        String[] arr = new String[jsonArray.size()];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = jsonArray.get(i).asString();
        }
        return arr;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String[] strs = stringToStringArray(line);

            String ret = new Solution3().longestCommonPrefix(strs);

            String out = (ret);

            System.out.print(out);
        }
    }
}

class Solution3 {
    public String longestCommonPrefix(String[] strs) {
        if(strs.length == 0 || strs == null){
            return "";
        }
        for(int i = 0; i < strs[0].length(); i++){
            char character = strs[0].charAt(i);
            for(int j = 1; j < strs.length; j++){
                if(i == strs[j].length() || strs[j].charAt(i) != character){
                    return strs[0].substring(0,i);
                }
            }
        }
        return strs[0];
    }
}
