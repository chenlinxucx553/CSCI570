package com.leetcode;

import java.util.*;

/**
 * Given a List of words, return the words that can be typed using letters of alphabet
 * on only one row's of American keyboard like the image below.
 *
 * @Author: Aaron Yang
 * @Date: 10/28/2018 10:36 AM
 */
public class KeyBoardRows {

    private Map<Integer, HashSet<Character>> map = new HashMap<>();

    {
        map.put(1, new HashSet<>(Arrays.asList('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p')));
        map.put(2, new HashSet<>(Arrays.asList('a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l')));
        map.put(3, new HashSet<>(Arrays.asList('z', 'x', 'c', 'v', 'b', 'n', 'm')));
    }

    public String[] findWords(String[] words) {
        List<String> result = new ArrayList<>();
        for (String word : words) {
            HashSet tempSet = assignSet(word.toCharArray()[0]);
            if (null != tempSet) {
                if (isContainAll(tempSet, word.toCharArray())) result.add(word);
            } else {
                continue;
            }
        }
        return result.toArray(new String[result.size()]);
    }

    private boolean isContainAll(HashSet tempSet, char[] chars) {
        for (char character : chars) {
            if (!tempSet.contains(Character.toLowerCase(character))) return false;
        }
        return true;
    }

    private HashSet assignSet(char c) {
        for (HashSet set : map.values()) {
            if (set.contains(Character.toLowerCase(c))) {
                return set;
            }
        }
        return null;
    }
}
