package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
 *
 * @Author: Aaron Yang
 * @Date: 11/19/2018 11:16 AM
 */
public class AverageOfLevelsInBinaryTree {

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

    public static String doubleArrayListToString(List<Double> nums) {
        return doubleArrayListToString(nums, nums.size());
    }

    public static String doubleArrayListToString(List<Double> nums, int length) {
        if (length == 0) {
            return "[]";
        }
        String result = "";
        for (int index = 0; index < length; index++) {
            Double number = nums.get(index);
            result += Double.toString(number) + ", ";
        }
        return "[" + result.substring(0, result.length() - 2) + "]";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            TreeNode t = stringToTreeNode(line);

            List<Double> list = new Solution115().averageOfLevels(t);

            String out = doubleArrayListToString(list);

            System.out.print(out);
        }
    }
}

class Solution115 {

    private List<Double> sum = new ArrayList<>();
    private List<Integer> count = new ArrayList<>();

    public List<Double> averageOfLevels(TreeNode root) {
        if (null == root) return new ArrayList<Double>();
        traverse(root, 0);
        for (int i = 0; i < sum.size(); i++)
            sum.set(i, sum.get(i) / count.get(i));
        return sum;
    }

    private void traverse(TreeNode node, int level) {
        if (null != node) {
            if (level < sum.size()) {
                sum.set(level, sum.get(level) + node.val);
                count.set(level, count.get(level) + 1);
            } else {
                sum.add(1.0 * node.val);
                count.add(1);
            }
            traverse(node.left, level + 1);
            traverse(node.right, level + 1);
        } else return;
    }
}