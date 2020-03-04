---
title: 50 Pow(x, n)
categories: 算法
icon: note
---

## 类型

`快速幂` `指数` `位运算`

## 思路及代码

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 特殊情况判断
        if n == 0:
            return 1
        elif n < 0:
            # 这里需要注意，如果是-2 **31，转成最大的正数 2 ** 31 - 1后，会少乘一次，因此需要单独处理
            if n == -2 ** 31:
                n = 2 ** 31 - 1
                return 1 / (self.fastPow(x, n) * x)
            else:
                n = -n
            return 1 / self.fastPow(x, n)

        else:
            return self.fastPow(x, n)

    # 快速幂法
    def fastPow(self, x, n):
        result = 1
        while n:
            # 从最低位的 x ^ 1 开始判断，n的二进制表示法表示在当前位是否需要乘。
            if n & 1:
                result *= x
            x *= x
            n >>= 1
        return result
```