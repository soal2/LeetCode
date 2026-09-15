# 全排列
# https://leetcode.cn/problems/permutations

"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
"""
import sys

def permute(nums: list[int]) -> list[list[int]]:
    res = []
    n = len(nums)
    path = [0] * n
    onPath = [False] * n

    def dfs(i):
        if i == n:
            res.append(path[:])
            return
        
        for j in range(n):
            if not onPath[j]:
                path[i] = nums[j]
                onPath[j] = True
                dfs(i + 1)
                onPath[j] = False
    dfs(0)
    return res

def main():
    data = sys.stdin.read().strip().splitlines()
    nums = list(map(int, data[0].split()))
    print(permute(nums=nums))

if __name__ == "__main__":
    main()
