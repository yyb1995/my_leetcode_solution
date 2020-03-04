---
title: 52 N皇后II
categories: 算法
icon: note
---

## 类型

`回溯`

## 思路及代码

### 个人思路

```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        # 特殊情况
        if n <= 0:
            return 0

        # 定义全局解
        result = 0

        # 路径使用全局变量储存，选择列表使用局部变量储存
        path = []

        # 定义回溯函数，选择列表
        def backtrack(line):
            # 回溯终点
            if line == n:
                # 在内层函数定义的变量需要
                nonlocal result
                result += 1
                return 

            # 对列进行遍历
            for col in range(n):
                # 判断有效性
                count = 0
                for i, j in path:
                    if j == col or line + col == i + j or line - col == i - j:
                        break
                    else:
                        count += 1
                # 有效
                if count == len(path):
                    # 加入路径
                    path.append((line, col))
                    backtrack(line + 1)
                    path.pop()
            
            return 

        backtrack(0)

        return result
```
