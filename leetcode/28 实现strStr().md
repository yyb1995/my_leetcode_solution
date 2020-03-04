---
title: 28 实现strStr()
categories: 算法
icon: note
---

## 类型

`字符串`

## 思路及代码

### 个人思路（暴力法，BF）

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 使用i，j双指针
        i, j = 0, 0
        hay_length = len(haystack)
        need_length = len(needle)
        # 如果目标字符串长度大于源字符串长度，直接返回-1
        if hay_length < need_length:
            return -1
        # 如果目标字符串长度为0，返回0
        if need_length == 0:
            return 0
        # 对源字符串进行遍历，这里需要防止越界问题
        while i <= hay_length - need_length:
            # 判断源字符串中一段是否与目标字符串完全相同
            while j < need_length and haystack[i] == needle[j]:
                i += 1
                j += 1
            # 如果完全相同，i = i + need_length, j = need_length，返回起点
            if j == need_length:
                return i - need_length
            # 如果部分匹配
            elif j > 0:
                # j表示匹配的长度，j - 1 表示起点后一位
                i -= j - 1
                j = 0
            # 如果没有匹配，i向前移动一位
            else:
                i += 1
        # 如果遍历后都无匹配，返回-1
        return -1
```
