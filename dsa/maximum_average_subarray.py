# LeetCode #643 - Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/
# Approach: Sliding Window | Time: O(n) | Space: O(1)


class Solution:
    def find_max_average(self, nums, k):
        current_sum = sum(nums[:k])
        max_sum = current_sum

        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, current_sum)

        return max_sum / k


if __name__ == "__main__":
    sol = Solution()
    print(sol.find_max_average([1, 12, -5, -6, 50, 3], 4))  # 12.75
    print(sol.find_max_average([5], 1))                       # 5.0
