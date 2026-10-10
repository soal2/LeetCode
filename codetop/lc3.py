"""
codetop.lc3 的 Docstring
https://leetcode.cn/problems/longest-substring-without-repeating-characters
"""
import sys
from collections import defaultdict

def lengthOfLongestSubstring(s: str) -> int:
    left = right = 0
    n = len(s)
    res = 0
    ht = defaultdict(int)
    while right < n:
        x = s[right]
        ht[x] += 1
        while ht[x] > 1:
            lx = s[left]
            ht[lx] -= 1
            left += 1
        res = max(res, right - left + 1)
        right += 1
    return res

def main():
    data = sys.stdin.read().strip().splitlines()
    s = data[0].strip().strip('"') if data else ""
    print(lengthOfLongestSubstring(s))

if __name__ == "__main__":
    main()