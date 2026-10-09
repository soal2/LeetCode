"""
回溯.Python.lc131 的 Docstring

https://leetcode.cn/problems/palindrome-partitioning
"""
import sys
def partition(s: str) -> list[list[str]]:
    n = len(s)
    res = []
    path = []
    def dfs(i: int) -> None:
        if i == n:
            res.append(path.copy())
            return
        
        for j in range(i, n):
            t = s[i:j + 1]
            if t[::] == t[::-1]:
                path.append(t)
                dfs(j + 1)
                path.pop()


    dfs(0)
    return res

def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    s = data[0].strip().strip('"')
    print(partition(s=s))

if __name__ == "__main__":
    main()