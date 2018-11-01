package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Given a binary search tree with non-negative values,
 * find the minimum absolute difference between values of any two nodes.
 *
 * @Author: Aaron Yang
 * @Date: 11/1/2018 9:59 AM
 */
public class MinimumDifferenceInBST {

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

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            TreeNode root = stringToTreeNode(line);

            int ret = new Solution96().getMinimumDifference(root);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution96 {
    private int min = Integer.MAX_VALUE;
    private Integer prev = Integer.MAX_VALUE;

    public int getMinimumDifference(TreeNode root) {
        if (null == root) return 0;
//        getDifference(root);

        getMinimumDifference(root.left);
        min = Math.min(min, Math.abs(root.val - prev));
        prev = root.val;
        getMinimumDifference(root.right);

        return min;
    }

    private void getDifference(TreeNode node) {
        if(null != node){
            getDifference(node.left);
            min = Math.min(min, Math.abs(node.val - prev));
            prev = node.val;
            getDifference(node.right);
        }
    }
}