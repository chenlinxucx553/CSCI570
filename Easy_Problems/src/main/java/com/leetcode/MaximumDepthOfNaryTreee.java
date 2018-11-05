package com.leetcode;

import java.util.List;

/**
 * Given a n-ary tree, find its maximum depth.
 * <p>
 * The maximum depth is the number of nodes along the longest path from
 * the root node down to the farthest leaf node.
 *
 * @Author: Aaron Yang
 * @Date: 11/5/2018 10:12 AM
 */
public class MaximumDepthOfNaryTreee {

    private int max = 0;

    public int maxDepth(Node3 root) {
        getDepth(root, 0);
        return max;
    }

    private void getDepth(Node3 node, int level) {
        if (null == node) {
            return;
        }
        max = Math.max(max, level + 1);
        for (Node3 item : node.children) {
            getDepth(item, level + 1);
        }
    }
}

class Node3 {
    public int val;
    public List<Node3> children;

    public Node3() {
    }

    public Node3(int _val, List<Node3> _children) {
        val = _val;
        children = _children;
    }
}