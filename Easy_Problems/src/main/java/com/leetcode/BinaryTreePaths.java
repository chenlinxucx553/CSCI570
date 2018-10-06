package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

/**
 * Given a binary tree, return all root-to-leaf paths.
 *
 * @Author: Aaron Yang
 * @Date: 10/6/2018 9:40 AM
 */
public class BinaryTreePaths {

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

    public static String stringListToString(List<String> stringList) {
        StringBuilder sb = new StringBuilder("[");
        for (String item : stringList) {
            sb.append(item);
            sb.append(",");
        }

        sb.setCharAt(sb.length() - 1, ']');
        return sb.toString();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            TreeNode root = stringToTreeNode(line);

            List<String> ret = new Solution51().binaryTreePaths(root);

            String out = stringListToString(ret);

            System.out.print(out);
        }
    }
}

class Solution51 {
    List<String> list = new ArrayList<>();
    String arrow = "->";


    public List<String> binaryTreePaths(TreeNode root) {
        if (null == root) return list;
        if (null != root.left) traverse(root.left, root.val + arrow);
        if (null != root.right) traverse(root.right, root.val + arrow);
        if (null == root.left && null == root.right) list.add(root.val + "");
        return list;
    }

    private void traverse(TreeNode node, String s) {
        StringBuffer buffer = new StringBuffer(s);
        if (null != node.left || null != node.right) {
            buffer.append(node.val + arrow);
            if (null != node.left) traverse(node.left, buffer.toString());
            if (null != node.right) traverse(node.right, buffer.toString());
        }else {
            buffer.append(node.val);
            list.add(buffer.toString());
        }
    }
}