# link https://leetcode.com/problems/contains-duplicate/

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        map = {}
        found = False
        for num in nums:
            if num in map:
                found = True
                break
            map[num] = num
        return found