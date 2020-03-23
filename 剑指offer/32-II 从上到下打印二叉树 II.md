---
title: 32-II 从上到下打印二叉树 II
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
        # 思路：BFS

        result = []
        stack = deque([root])

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
                result.append(current_layer)
        return result
```
