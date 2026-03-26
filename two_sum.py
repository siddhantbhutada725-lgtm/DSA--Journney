class solutions
    def twoSums(self,nums,target):
        seen_numbers={}
        for i,nums in enumerate(nums):
            complement = target - nums
            if complement in seen_numbers:
                return [seen_numbers[compliment],i]
            seen_numbers[nums]=i