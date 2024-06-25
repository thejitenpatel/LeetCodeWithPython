from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left_pointer = 0
        right_pinter = len(height) - 1
        max_area = 0

        while left_pointer < right_pinter:
            w = right_pinter - left_pointer
            h = min(height[left_pointer], height[right_pinter])
            a = w * h
            max_area = max(max_area, a)

            if height[left_pointer] < height[right_pinter]:
                left_pointer += 1
            else:
                right_pinter -= 1
        
        return max_area
    
solution = Solution()
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
            
