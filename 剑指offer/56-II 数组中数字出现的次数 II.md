---
title: 56-II 数组中数字出现的次数 II
categories: 算法
icon: note
---

## 类型

`位运算`

## 思路及代码

### 个人思路

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        current_loc = 1
        for i in range(32):
            count = 0
            for num in nums:
                if num & current_loc:
                    count += 1
            if count % 3 != 0:
                result |= current_loc
            current_loc <<= 1

        return result - 2 ** 32 if result > 2 ** 31 - 1 else result 
```
