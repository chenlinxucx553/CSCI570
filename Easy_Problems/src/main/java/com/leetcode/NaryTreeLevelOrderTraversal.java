package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * Given an n-ary tree, return the level order traversal of its nodes' values.
 * (ie, from left to right, level by level).
 *
 * @Author: Aaron Yang
 * @Date: 10/17/2018 4:05 PM
 */
public class NaryTreeLevelOrderTraversal {

    private List<List<Integer>> result = new ArrayList<>();

    public List<List<Integer>> levelOrder(Node2 root) {
        if (null != root) {
            ArrayList<Integer> list = new ArrayList<>();
            list.add(root.val);
            result.add(list);
            traversal(root.children);
        }
        return result;
    }

    private void traversal(List<Node2> children) {
        List<Node2> next = new ArrayList<>();
        if (null != children) {
            List<Integer> list = new ArrayList<>();
            for (Node2 node : children) {
                list.add(node.val);
                for (Node2 child : node.children) {
                    next.add(child);
                }
            }
            if (!list.isEmpty()) result.add(list);
        }
        if (!next.isEmpty()) traversal(next);
    }
}

class Node2 {
    public int val;
    public List<Node2> children;

    public Node2() {
    }

    public Node2(int _val, List<Node2> _children) {
        val = _val;
        children = _children;
    }
}