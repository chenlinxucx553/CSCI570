package com.leetcode;

import java.util.*;

/**
 * Suppose Andy and Doris want to choose a restaurant for dinner,
 * and they both have a list of favorite restaurants represented by strings.
 * <p>
 * You need to help them find out their common interest with the least list index sum.
 * If there is a choice tie between answers, output all of them with no order requirement.
 * You could assume there always exists an answer.
 *
 * @Author: Aaron Yang
 * @Date: 11/16/2018 10:03 AM
 */
public class MinimumIndexSumOfTwoLists {

    public String[] findRestaurant(String[] list1, String[] list2) {
        HashSet<String> set1 = list2Set(list1);
        HashSet<String> set2 = list2Set(list2);
        set1.retainAll(set2);
        return set2List(set1, list1, list2);
    }

    private <T> HashSet<T> list2Set(T[] list) {
        HashSet<T> set = new HashSet<>();
        for (T item : list) {
            set.add(item);
        }
        return set;
    }

    public String[] set2List(HashSet<String> set, String[] list1, String[] list2) {
        if (set.size() == 1) return new String[]{set.iterator().next()};
        else {
            Map map = new HashMap<String, Integer>();
            int min = Integer.MAX_VALUE;
            List array = new ArrayList<String>();
            for (String str : set) {
                int indexSum = getSum(str, list1, list2);
                min = Math.min(indexSum, min);
                map.putIfAbsent(str, indexSum);
            }
            Iterator<Map.Entry<String, Integer>> iterator = map.entrySet().iterator();
            while (iterator.hasNext()) {
                Map.Entry<String, Integer> entry = iterator.next();
                if (entry.getValue() == min) array.add(entry.getKey());
            }
            return (String[]) array.toArray(new String[array.size()]);
        }
    }

    private int getSum(String str, String[] list1, String[] list2) {
        for (int i = 0; i < list1.length; i++) {
            if (str.equals(list1[i])) {
                for (int j = 0; j < list2.length; j++) {
                    if (str.equals(list2[j])) return i + j;
                }
            }
        }
        return 0;
    }


}
