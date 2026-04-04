# LeetCode #125 - Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Approach: Two Pointers | Time: O(n) | Space: O(n)


class Solution:
    def is_palindrome(self, s):
        cleaned = "".join(char.lower() for char in s if char.isalnum())

        left = 0
        right = len(cleaned) - 1

        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    sol = Solution()
    print(sol.is_palindrome("A man, a plan, a canal: Panama"))  # True
    print(sol.is_palindrome("race a car"))                       # False
    print(sol.is_palindrome(" "))                                 # True
