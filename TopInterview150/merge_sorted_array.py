from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Start merging from the end of both arrays
        index1 = m - 1
        index2 = n - 1
        merge_index = m + n - 1

        while index1 >= 0 and index2 >= 0:
            if nums1[index1] > nums2[index2]:
                nums1[merge_index] = nums1[index1]
                index1 -= 1
            else:
                nums1[merge_index] = nums2[index2]
                index2 -= 1
            merge_index -= 1

        # If there are remaining elements in nums2, they are already sorted
        # and can be directly copied to nums1
        while index2 >= 0:
            nums1[merge_index] = nums2[index2]
            index2 -= 1
            merge_index -= 1

    def test_merge(self):
        # Test case 1
        nums1_case1 = [1, 2, 3, 0, 0, 0]
        m_case1 = 3
        nums2_case1 = [2, 5, 6]
        n_case1 = 3
        self.merge(nums1_case1, m_case1, nums2_case1, n_case1)
        assert nums1_case1 == [1, 2, 2, 3, 5, 6], "Test case 1 failed"

        # Test case 2
        nums1_case2 = [1]
        m_case2 = 1
        nums2_case2 = []
        n_case2 = 0
        self.merge(nums1_case2, m_case2, nums2_case2, n_case2)
        assert nums1_case2 == [1], "Test case 2 failed"

        # Test case 3
        nums1_case3 = [0]
        m_case3 = 0
        nums2_case3 = [1]
        n_case3 = 1
        self.merge(nums1_case3, m_case3, nums2_case3, n_case3)
        assert nums1_case3 == [1], "Test case 3 failed"

        # Test case 4 (Additional test case)
        nums1_case4 = [4, 5, 6, 0, 0, 0]
        m_case4 = 3
        nums2_case4 = [1, 2, 3]
        n_case4 = 3
        self.merge(nums1_case4, m_case4, nums2_case4, n_case4)
        assert nums1_case4 == [1, 2, 3, 4, 5, 6], "Test case 4 failed"

        print("All test cases passed successfully!")


sol = Solution()
sol.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
sol.test_merge()
