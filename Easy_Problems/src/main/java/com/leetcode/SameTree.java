package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/**
 * Given two binary trees, write a function to check if they are the same or not.
 *
 * @Author: Aaron Yang
 * @Date: 9/16/2018 10:17 AM
 */
public class SameTree {
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

    public static String booleanToString(boolean input) {
        return input ? "True" : "False";
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = in.readLine()) != null) {
            TreeNode p = stringToTreeNode(line);
            line = in.readLine();
            TreeNode q = stringToTreeNode(line);

            boolean ret = new Solution18().isSameTree(p, q);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution18 {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if ((null != p && null != q) && p.val == q.val) {
            if (null != p.left && null != q.left) {
                if(!isSameTree(p.left, q.left)){
                    return false;
                }
            } else if ((null == p.left && null != q.left) || (null != p.left && null == q.left)) {
                return false;
            }

            if (null != p.right && null != q.right) {
                if(!isSameTree(p.right, q.right)){
                    return false;
                }
            } else if ((null == p.right && null != q.right) || (null != p.right && null == q.right)) {
                return false;
            }
            return true;
        }else if(null == p && null == q){
            return true;
        }
        return false;
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int x) {
        val = x;
    }
}
