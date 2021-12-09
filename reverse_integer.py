#Reverse Integer
#  Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
#
#
# Example 1:
#
# Input: x = 123
# Output: 321
# Example 2:
#
# Input: x = -123
# Output: -321
# Example 3:
#
# Input: x = 120
# Output: 21
# Example 4:
#
# Input: x = 0
# Output: 0
#
#
# Constraints:
#
# -231 <= x <= 231 - 1
import math

import numpy as np


class Solution:
    def reverse(self, x: int) -> int:
        sign = np.sign(x)

        a = abs(x)
        num = [int(i) for i in str(a)]
        numbers = num[::-1]
        ll = [str(number) for number in numbers]
        y = "".join(ll)
        integer = int(y)*sign

        if int(y) < math.pow(2,31):
            return integer
        else:
            return 0