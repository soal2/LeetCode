# 电话号码的字母组合
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number

"""
回溯.Python.lc17 的 Docstring

给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
"""
import sys

MAPPING = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

def letterCombinations(digits: str) -> list[str]:
    res = []
    n = len(digits)
    path = [''] * n

    if n == 0:
        return res

    def dfs(i):
        if i == n:
            res.append("".join(path[:]))
            return
        
        for j, x in enumerate(MAPPING[int(digits[i])]):
            path[i] = x
            dfs(i + 1)
    dfs(0)
    return res

def main():
    data = sys.stdin.read().strip().splitlines()
    digits = list(map(str, data[0].strip()))
    print(letterCombinations(digits=digits))

if __name__ == "__main__":
    main()