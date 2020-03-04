---
title: 8 字符串转换整数(atoi)
categories: 算法
icon: note
---

## 类型

`正则`

## 思路及代码

正则表达式匹配。

```python
import re
class Solution:
    def myAtoi(self, str1: str) -> int:
        return max(min(int(*re.findall('^[\+\-]?\d+', str1.lstrip())), 2**31 - 1), -2**31)
```
