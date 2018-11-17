package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.LinkedList;
import java.util.Queue;

/**
 * You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.  The null node needs to be represented by empty parenthesis pair "()". And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between the string and the original binary tree.
 *
 * @Author: Aaron Yang
 * @Date: 11/17/2018 10:56 AM
 */
public class ConstructStringFromBinaryTree {

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
            TreeNode t = stringToTreeNode(line);

            String ret = new Solution112().tree2str(t);

            String out = (ret);

            System.out.print(out);
        }
    }
}

class Solution112 {

    public String tree2str(TreeNode t) {
        if (t == null) return "";
        StringBuffer buffer = new StringBuffer();
        traverse(t, buffer);
        return buffer.toString();
    }

    private void traverse(TreeNode node, StringBuffer sb) {
        sb.append(node.val);
        if (node.left != null) {
            sb.append("(");
            traverse(node.left, sb);
            sb.append(")");
        } else if (node.right != null) {
            sb.append("()");
        }
        if (node.right != null) {
            sb.append("(");
            traverse(node.right, sb);
            sb.append(")");
        }
    }
}