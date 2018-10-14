package com.leetcode;

import sun.reflect.generics.tree.Tree;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Find the sum of all left leaves in a given binary tree.
 *
 * @Author: Aaron Yang
 * @Date: 10/14/2018 11:20 AM
 */
public class SumOfLeftLeaves {

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

            int ret = new Solution71().sumOfLeftLeaves(root);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution71 {
    int sum = 0;

    public int sumOfLeftLeaves(TreeNode root) {
        if (root == null) return 0;
        traverse(root);
        return sum;
    }

    private void traverse(TreeNode root) {
        if (null != root.left || null != root.right) {
            TreeNode left = root.left;
            if (null != left && left.left == null && left.right == null) sum += left.val;
            else if (null != root.left) traverse(root.left);
            if (null != root.right) traverse(root.right);
        }
    }
}