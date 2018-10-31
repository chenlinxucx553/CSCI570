package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/**
 * Given a word, you need to judge whether the usage of capitals in it is right or not.
 * We define the usage of capitals in a word to be right when one of the following cases holds:
 * All letters in this word are capitals, like "USA".
 * All letters in this word are not capitals, like "leetcode".
 * Only the first letter in this word is capital if it has more than one letter, like "Google".
 * <p>
 * Otherwise, we define that this word doesn't use capitals in a right way.
 *
 * @Author: Aaron Yang
 * @Date: 10/31/2018 12:11 PM
 */
public class DetectCaptical {

    public static String stringToString(String input) {
        return JsonArray.readFrom("[" + input + "]").get(0).asString();
    }

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            String word = stringToString(line);

            boolean ret = new Solution95().detectCapitalUse(word);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution95 {
    public boolean detectCapitalUse(String word) {
        if (word.equals(word.toLowerCase())) return true;
        else if (word.equals(word.toUpperCase())) return true;
        else {
            if (word.toCharArray()[0] != Character.toUpperCase(word.toCharArray()[0])) return false;
            String remain = word.substring(1, word.length());
            if (remain.equals(remain.toLowerCase())) return true;
            else return false;
        }
    }
}