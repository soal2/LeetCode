"""
回溯.Python.lc79 的 Docstring

https://leetcode.cn/problems/word-search
"""

import sys

def exist(board: list[list[str]], word: str) -> bool:
    m, n = len(board), len(board[0])
    def dfs(i, j, k):
        if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]: return False
        if k == len(word) - 1:
            return True
        board[i][j] = ''
        res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j - 1, k + 1) or dfs(i, j + 1, k + 1)
        board[i][j] = word[k]
        return res
    
    return any(dfs(i, j, 0) for i in range(m) for j in range(n))

def main():
    data = [line for line in sys.stdin.read().splitlines() if line.strip()]
    word = data[-1].strip()
    board = [line.split() for line in data[:-1]]
    print(exist(board=board, word=word))

if __name__ == "__main__":
    main()