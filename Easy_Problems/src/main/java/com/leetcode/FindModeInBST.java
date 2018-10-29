package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.
 *
 * @Author: Aaron Yang
 * @Date: 10/29/2018 10:02 AM
 */
public class FindModeInBST {

    public static TreeNode stringToTreeNode(String input) {
        input = input.trim();
        input = input.substring(1, input.length() - 1);
        if (input.length() == 0) {
            return null;
        }

        String[] parts = input.split(",");
        String item = parts[0];
        TreeNode root = new TreeNode(Integer.parseInt(item));
        Queue<TreeNode> nodeQueue = new LinkedList<>();
        nodeQueue.add(root);

        int index = 1;
        while (!nodeQueue.isEmpty()) {
            TreeNode node = nodeQueue.remove();

            if (index == parts.length) {
                break;
            }

            item = parts[index++];
            item = item.trim();
            if (!item.equals("null")) {
                int leftNumber = Integer.parseInt(item);
                node.left = new TreeNode(leftNumber);
                nodeQueue.add(node.left);
            }

            if (index == parts.length) {
                break;
            }

            item = parts[index++];
            item = item.trim();
            if (!item.equals("null")) {
                int rightNumber = Integer.parseInt(item);
                node.right = new TreeNode(rightNumber);
                nodeQueue.add(node.right);
            }
        }
        return root;
    }

    public static String integerArrayToString(int[] nums, int length) {
        if (length == 0) {
            return "[]";
        }

        String result = "";
        for (int index = 0; index < length; index++) {
            int number = nums[index];
            result += Integer.toString(number) + ", ";
        }
        return "[" + result.substring(0, result.length() - 2) + "]";
    }

    public static String integerArrayToString(int[] nums) {
        return integerArrayToString(nums, nums.length);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            TreeNode root = stringToTreeNode(line);

            int[] ret = new Solution92().findMode(root);

            String out = integerArrayToString(ret);

            System.out.print(out);
        }
    }
}

class Solution92 {
    //---------Time Limit Exceeded
//    private Map<Integer, Integer> map = new HashMap<>();
//
//    public int[] findMode(TreeNode root) {
//        if (null != root) {
//            if (map.containsKey(root.val)) map.replace(root.val, map.get(root.val) + 1);
//            map.putIfAbsent(root.val, 1);
//            if (null != root.left) findMode(root.left);
//            if (null != root.right) findMode(root.right);
//        }
//        int max = 0;
//        for (int value : map.values()) {
//            max = Math.max(value, max);
//        }
//        List<Integer> list = new ArrayList<>();
//        Iterator<Map.Entry<Integer, Integer>> it = map.entrySet().iterator();
//        while (it.hasNext()) {
//            Map.Entry<Integer, Integer> entry = it.next();
//            if (entry.getValue() == max) {
//                list.add(entry.getKey());
//            }
//        }
//        return list2Array(list);
//    }
//
    private int[] list2Array(List<Integer> list) {
        int[] array = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            array[i] = list.get(i);
        }
        return array;
    }

    private List<Integer> list = new ArrayList<>();
    private int curCount = 1;
    private int maxCount = 0;
    private Integer preValue;

    public int[] findMode(TreeNode root) {
        traverse(root);
        return list2Array(list);
    }

    private void traverse(TreeNode root) {
        if (null == root) return;
        traverse(root.left);
        if (null != preValue) {
            if (root.val == preValue) {
                curCount++;
            } else {
                curCount = 1;
            }
        }

        if (curCount > maxCount) {
            maxCount = curCount;
            list.clear();
            list.add(root.val);
        } else if (curCount == maxCount) {
            list.add(root.val);
        }

        preValue = root.val;
        traverse(root.right);
    }
}