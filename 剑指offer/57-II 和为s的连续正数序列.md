---
title: 57-II 和为s的连续正数序列
categories: 算法
icon: note
---

## 类型

`数组`

## 思路及代码

### 个人思路

```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        result = []
        for start in range(1, target):
            for k in range(2, target + 1):
                if k * k + (2 * start - 1) * k == 2 * target:
                    result.append([start + item for item in range(k)])
                elif k * k + (2 * start - 1) * k > 2 * target:
                    break
        
        return result
```

### 通过二次函数公式得到的结果

```python
from math import sqrt
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        i, res = 1, []
        
        # 根据上面的条件1，限定i的大小，即间隔的范围
        while i*(i+1) / 2 < target:
            # 根据条件2，如果x不 为整数则扩大间隔
            if not (target - i*(i+1) / 2) % (i+1):
                # 当//中有不是整数的值时，//得到的结果是float
                x = int((target - i*(i+1)/2) // (i + 1)
                # 反推出y，将列表填入输出列表即可
                res.append(list(range(x,x + i + 1)))
            # 当前间隔判断完毕，检查下一个间隔
            i += 1

        # 由于间隔是从小到大，意味着[x,y]列表是从大到小的顺序放入输出列表res的，所以反转之
        return res[::-1]
```
