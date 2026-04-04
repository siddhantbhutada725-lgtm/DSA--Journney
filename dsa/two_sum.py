# LeetCode #1 - Two Sum
# https://leetcode.com/problems/two-sum/
# Approach: Hash Map | Time: O(n) | Space: O(n)


class Solution:
    def two_sum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    sol = Solution()
    print(sol.two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(sol.two_sum([3, 2, 4], 6))       # [1, 2]
    print(sol.two_sum([3, 3], 6))           # [0, 1]
