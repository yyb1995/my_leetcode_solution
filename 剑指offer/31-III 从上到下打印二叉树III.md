---
title: 31-III 从上到下打印二叉树III
categories: 算法
icon: note
---

## 类型

`二叉树` `BFS`

## 思路及代码

### 个人思路

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        stack = deque()
        stack.append(root)
        layer_num = 0

        while stack:
            current_layer = []
            for i in range(len(stack)):
                current_node = stack.popleft()
                if current_node:
                    current_layer.append(current_node.val)
                    if current_node.left:
                        stack.append(current_node.left)
                    if current_node.right:
                        stack.append(current_node.right)
            if current_layer:
                if layer_num & 1:
                    result.append(current_layer[::-1])
                else:
                    result.append(current_layer)
            layer_num += 1
        return result

```
