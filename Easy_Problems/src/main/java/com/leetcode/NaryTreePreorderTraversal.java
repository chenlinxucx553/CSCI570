package com.leetcode;

import java.util.ArrayList;
import java.util.List;

/**
 * Given an n-ary tree, return the preorder traversal of its nodes' values.
 *
 * @Author: Aaron Yang
 * @Date: 11/9/2018 9:48 AM
 */
public class NaryTreePreorderTraversal {

    private List<Integer> result = new ArrayList();

    public List<Integer> preorder(Node2 root) {
        if (null != root) {
            result.add(root.val);
        } else {
            return new ArrayList();
        }
        if (null != root.children) {
            for (Node2 node : root.children) {
                preorder(node);
            }
        }
        return result;
    }
}
