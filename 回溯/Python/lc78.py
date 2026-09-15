# 子集
# https://leetcode.cn/problems/subsets

"""
回溯.Python.lc78 的 Docstring

给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
"""

import sys

def subsets(nums: list[int]) -> list[list[int]]:
    res = []
    path = []
    n = len(nums)

    def dfs(i: int):
        if i == n:
            res.append(path[:])
            return
        
        # 不选
        dfs(i + 1)

        x = nums[i]
        path.append(x)
        dfs(i + 1)
        path.pop()

    dfs(0)
    return res

def main():
    data = sys.stdin.read().strip().splitlines()
    nums = list(map(int, data[0].split()))

    print(subsets(nums=nums))

if __name__ == "__main__":
    main()