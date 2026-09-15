# 括号生成(*)
# https://leetcode.cn/problems/generate-parentheses

"""
回溯.Python.lc22 的 Docstring
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
"""

import sys

def generateParenthesis(n: int) -> list[str]:
    res = []
    path = [''] * n * 2
    
    def dfs(leftn, rightn):
        if rightn == n:
            res.append("".join(path[:]))
            return

        if leftn < n:
            path[leftn + rightn] = '('
            dfs(leftn + 1, rightn)
        if rightn < leftn:
            path[leftn + rightn] = ')'
            dfs(leftn, rightn + 1)
        
    dfs(0, 0)
    return res



def main():
    num = input("输入n:")
    print(generateParenthesis(n=int(num)))

if __name__ == "__main__":
    main()