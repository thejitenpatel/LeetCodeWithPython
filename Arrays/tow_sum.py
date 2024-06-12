from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        number_of_index = {}

        for index, num in enumerate(nums):
            complement = target - num

            if complement in number_of_index:
                return [number_of_index[complement], index]
        
            number_of_index[num] = index

solution = Solution()
print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
