package com.leetcode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Stack;

/**
 * Given an n-ary tree, return the postorder traversal of its nodes' values.
 *
 * @Author: Aaron Yang
 * @Date: 11/9/2018 10:03 AM
 */
public class NaryTreePostorderTreaversal {

    LinkedList<Node2> stack = new LinkedList<>();
    LinkedList<Integer> result = new LinkedList<>();

    public List<Integer> postorder(Node2 root) {
        if (null == root) return new ArrayList<>();
        else {
            stack.add(root);

            while (!stack.isEmpty()) {
                Node2 node = stack.pollLast();
                result.addFirst(node.val);
                for (Node2 node2 : node.children) {
                    stack.add(node2);
                }
            }
        }
        return result;
    }
}
