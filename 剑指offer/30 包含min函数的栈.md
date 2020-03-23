---
title: 30 包含min函数的栈
categories: 算法
icon: note
---

## 类型

`栈` `动态规划`

## 思路及代码

### 个人思路

```python
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main = []
        self.dp =[]


    def push(self, x: int) -> None:
        self.main.append(x)
        if not self.dp:
            self.dp.append(x)
        else:
            self.dp.append(min(x, self.dp[-1]))


    def pop(self) -> None:
        if self.main:
            self.dp.pop()
            return self.main.pop()

    def top(self) -> int:
        if self.main:
            return self.main[-1]

    def min(self) -> int:
        if self.main:
            return self.dp[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
```
