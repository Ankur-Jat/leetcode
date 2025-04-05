from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
    
        def XOR_sum( nums: List[int], index: int, current_XOR: int) -> int:
            if index == len(nums): return current_XOR
            with_element = XOR_sum(nums, index + 1, current_XOR ^ nums[index])
            without_element = XOR_sum(nums, index + 1, current_XOR)
            return with_element + without_element
        return XOR_sum(nums, 0, 0)


def test():
    s = Solution()
    assert s.subsetXORSum([1, 3]) == 6
    assert s.subsetXORSum([5, 1, 6]) == 28
    assert s.subsetXORSum([3, 2, 1, 5]) == 28
    assert s.subsetXORSum([2, 4, 5]) == 31
    assert s.subsetXORSum([0]) == 0
    print("All test cases pass")

if __name__ == "__main__":
    test()
