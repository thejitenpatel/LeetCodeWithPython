from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        current_altitude = 0

        highest_altitude = current_altitude

        for g in gain:

            current_altitude += g

            if current_altitude > highest_altitude:
                highest_altitude = current_altitude

        return highest_altitude


sol = Solution()
print(sol.largestAltitude(gain=[-5, 1, 5, 0, -7]))
