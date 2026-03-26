class Solution:
    def twoSum(self, nums, target):
        # Finger 1: Starts at the beginning
        for i in range(len(nums)):
            # Finger 2: Scans the lockers ahead of Finger 1
            for j in range(i + 1, len(nums)):
                # If they add up to the target, return their indices
                if nums[i] + nums[j] == target:
                    return [i, j]