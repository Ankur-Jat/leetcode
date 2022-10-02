"""
Leetcode: https://leetcode.com/problems/minimize-xor/
Date: 2-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
class Solution(object):
    def minimizeXor(self, num1, num2):
        """
        :type num1: int
        :type num2: int
        :rtype: int
        """
        def setRightBit(num):
            return num - (num & (~num + 1))
        
        def bitCount(num):
            counter = 0
            while num:
                num = setRightBit(num)
                counter += 1
            return counter

        num1Bits = bitCount(num1)
        num2Bits = bitCount(num2)
        if num2Bits == num1Bits:
            return num1
        
        if num2Bits < num1Bits:
            diff = num1Bits - num2Bits
            while diff:
                num1 = setRightBit(num1)
                diff -= 1
            return num1
        
        num1Bin = bin(num1)[2:]
        diff = num2Bits - num1Bits
        num1BinIndex = len(num1Bin) - 1
        while num1BinIndex >= 0 and diff > 0:
            if num1Bin[num1BinIndex] == '0':
                num1Bin = num1Bin[:num1BinIndex] + '1' + num1Bin[num1BinIndex+1:]
                diff -= 1
            num1BinIndex -= 1
        while diff:
            num1Bin = '1' + num1Bin
            diff -= 1
        return int(num1Bin, 2)
        

def test():
    solution = Solution()
    test_cases = [
        [ 3, 5, 3, ],
        [ 16, 15, 23, ],
        [ 15, 16, 8, ],
    ]
    for index, test_case in enumerate(test_cases):
        assert solution.minimizeXor(test_case[0], test_case[1]) == test_case[2], 'test case number {} is failing'.format(index)


if __name__ == '__main__':
    test()
