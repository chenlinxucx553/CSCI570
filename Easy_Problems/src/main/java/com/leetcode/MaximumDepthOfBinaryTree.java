package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Given a binary tree, find its maximum depth.
 *
 * @Author: Aaron Yang
 * @Date: 9/17/2018 9:11 AM
 */
public class MaximumDepthOfBinaryTree {

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

            int ret = new Solution20().maxDepth(root);

            String out = String.valueOf(ret);

            System.out.print(out);
        }
    }
}

class Solution20 {
    public int maxDepth(TreeNode root) {
        if (null == root) return 0;
        return Math.max(getDepth(root.left, 1), getDepth(root.right, 1));
    }

    int getDepth(TreeNode root, int result) {
        if (null != root) {
            result += 1;
            if (null != root.left) {
                int leftDepth = getDepth(root.left, result);
                if (null != root.right) {
                    return Math.max(leftDepth, getDepth(root.right, result));
                }
                return leftDepth;
            }
            if (null != root.right) return getDepth(root.right, result);
        }
        return result;
    }
}