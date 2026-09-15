import sys
# 组合总和2
# https://leetcode.cn/problems/combination-sum-ii

"""
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。 

"""
def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    candidates.sort()
    res = []
    path = []
    n = len(candidates)

    def dfs(i: int, target: int):
        if target == 0:
            res.append(path.copy())
            return
        
        if i == n or target < 0:
            return
        
        
        # 选
        x = candidates[i]
        path.append(x)
        dfs(i + 1, target - x) # 选完之后当前的元素就需要跳过了
        path.pop()

        # 不选
        i += 1
        while i < n and candidates[i] == x:
            i += 1
        dfs(i, target)

    dfs(0, target)
    return res

def main():
    data = sys.stdin.read().strip().splitlines()
    if not data:
        return
    print(data)
    candidates = list(map(int, data[0].split()))
    target = int(data[1].strip())

    print(combinationSum(candidates=candidates, target=target))

if __name__ == "__main__":
    main()