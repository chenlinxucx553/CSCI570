package com.leetcode;

import com.eclipsesource.json.JsonArray;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

/**
 * Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
 *
 * @Author: Aaron Yang
 * @Date: 10/12/2018 11:36 AM
 */
public class RansomNote {

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
            String ransomNote = stringToString(line);
            line = in.readLine();
            String magazine = stringToString(line);

            boolean ret = new Solution66().canConstruct(ransomNote, magazine);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution66 {
    public boolean canConstruct(String ransomNote, String magazine) {

        if(ransomNote.isEmpty() && magazine.isEmpty()) return true;
        else if(!ransomNote.isEmpty() && magazine.isEmpty())return false;
        else if(ransomNote.isEmpty() && !magazine.isEmpty())return true;

        HashMap<Character,Integer> magazineMap = new HashMap<Character, Integer>();
        HashMap<Character,Integer> ransomMap = new HashMap<Character, Integer>();
        int frequency = 0;
        for(int i= 0, j = 0; i < magazine.length() || j < ransomNote.length(); i++, j++){
            if(i < magazine.length()){
                char m = magazine.charAt(i);
                if(magazineMap.containsKey(m)){
                    frequency = magazineMap.get(m) + 1;
                    magazineMap.put(m,frequency);
                }else{
                    magazineMap.put(m,1);
                }
            }
            if(j < ransomNote.length()){
                char r = ransomNote.charAt(j);
                if(ransomMap.containsKey(r)){
                    frequency = ransomMap.get(r) + 1;
                    ransomMap.put(r,frequency);
                }else{
                    ransomMap.put(r,1);
                }
            }
        }

        for(Character ch : ransomMap.keySet()){
            frequency = ransomMap.get(ch);
            if(!magazineMap.containsKey(ch)){
                return false;
            }else if(frequency > magazineMap.get(ch)){
                return false;
            }
        }
        return true;
    }
}
