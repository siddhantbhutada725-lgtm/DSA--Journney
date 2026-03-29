class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        cleaned_string=""
        for char in s:
            if char.isalnum():
                cleaned_string+=char.lower()
        left=0
        right = len(cleaned_string) - 1
        while left < right:
            if cleaned_string[left]!= cleaned_string[right]:
                return False
            left+=1
            right-=1
        return True