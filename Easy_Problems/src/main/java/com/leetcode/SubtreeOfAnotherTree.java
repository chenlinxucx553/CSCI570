package com.leetcode;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

/**
 * Given two non-empty binary trees s and t,
 * check whether tree t has exactly the same structure and node values with a subtree of s.
 * <p>
 * A subtree of s is a tree consists of a node in s and all of this node's descendants.
 * <p>
 * The tree s could also be considered as a subtree of itself.
 *
 * @Author: Aaron Yang
 * @Date: 11/6/2018 11:03 AM
 */
public class SubtreeOfAnotherTree {


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
            TreeNode s = stringToTreeNode(line);
            line = in.readLine();
            TreeNode t = stringToTreeNode(line);

            boolean ret = new Solution106().isSubtree(s, t);

            String out = booleanToString(ret);

            System.out.print(out);
        }
    }
}

class Solution106 {

    public boolean isSubtree(TreeNode s, TreeNode t) {
        Stack<TreeNode> st = new Stack<>();
        st.push(s);
        while(!st.isEmpty()) {
            TreeNode tmp = st.pop();
            if(tmp.left != null) st.push(tmp.left);
            if(tmp.right != null) st.push(tmp.right);
            if(tmp.val == t.val && isST(tmp, t)) return true;
        }
        return false;
    }
    private boolean isST(TreeNode n, TreeNode t) {
        if(n == null && t == null) return true;
        if(n == null && t != null || n != null && t == null || n.val != t.val) return false;
        boolean bl = isST(n.left, t.left);
        boolean br = isST(n.right, t.right);
        return br&bl;
    }
}