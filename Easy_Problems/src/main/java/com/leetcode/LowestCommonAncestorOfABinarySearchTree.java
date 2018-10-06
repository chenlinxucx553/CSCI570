package com.leetcode;

/**
 * Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
 * <p>
 * <p>
 * According to the definition of LCA on Wikipedia:
 * “The lowest common ancestor is defined between two nodes p and q
 * as the lowest node in T that has both p and q as descendants
 * (where we allow a node to be a descendant of itself).”
 * <p>
 * <p>
 * Given binary search tree:  root = [6,2,8,0,4,7,9,null,null,3,5]
 * All of the nodes' values will be unique.
 * p and q are different and both values will exist in the BST.
 *
 * @Author: Aaron Yang
 * @Date: 10/5/2018 5:10 PM
 */
public class LowestCommonAncestorOfABinarySearchTree {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        if (null == root) return null;
        if (Math.max(p.val, q.val) < root.val) return lowestCommonAncestor(root.left, p, q);
        if (Math.min(p.val, q.val) > root.val) return lowestCommonAncestor(root.right, p, q);
        return root;
    }
}
