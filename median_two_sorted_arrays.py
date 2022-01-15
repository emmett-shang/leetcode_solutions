from typing import List

import math

nums1 = [1, 3]
nums2 = [2]

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:




        combine = [nums1 + nums2]
        flat_combine = sum(combine, [])
        flat_combine.sort()
        if len(flat_combine) % 2 != 0:
            median_odd = flat_combine[math.ceil(len(flat_combine) / 2 - 1) ]


            return median_odd

        if len(flat_combine) % 2 == 0:
            half = flat_combine[math.ceil(len(flat_combine) / 2 - 1)]
            median_even = (half + flat_combine[math.ceil(len(flat_combine) / 2)]) / 2


            return median_even

sol = Solution()
print(sol.findMedianSortedArrays(nums1, nums2))



