"""
Leetcode: https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/
Date: 2-Oct-2023
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)

# Intuition
1. To win the game Alice needs more turn than Bob because she has to play first.
2. To play the turn each player needs at least 3 consicutive chars of their type, "A" for Alice, and "B" for Bob.
3. If player has X consecutive char of their type, where X > 2, then they will delete one which means now there will be (X - 1) consicutive chars left and they can use the remaining conseccutive chars to play their next turn only if this ( X - 1 ) is greater than 2. 
4. Which means if X > 2 then the players can use that sequence for ( X - 2 ) times.

# Approach
1. As per the intutitions its clear that we have to keep counting all such consecutive pairs of the same char where the count is greatar then 2.
2. Then Alice will win only if her chars count (meeting above stated constraints) is greatar than Bob.

# Complexity
- Time complexity:
Because we are just iterating once so the time complexity is O(n) where n is the length of the String.

- Space complexity:
O(1) because we are not consuimg any extra space.
"""


class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        charASum = charBSum = 0
        currChar, currCounter = colors[0], 1

        for char in colors[1:]:
            if char == currChar:
                currCounter += 1
            else:
                if currChar == 'A':
                    charASum += max(0, currCounter - 2)
                else:
                    charBSum += max(0, currCounter - 2)
                currCounter = 1
                currChar = char
        if currChar == 'A':
            charASum += max(0, currCounter - 2)
        else:
            charBSum += max(0, currCounter - 2)
        return charASum > charBSum


def test():
    testcases = [
        ["AAABABB", True],
        ["AA", False],
        ["ABBBBBBBAAA", False],
        ["AAAABBBB", False]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.winnerOfGame(testcase[0])
        assert result == testcase[1], 'Testcase #{} failed! Expected: {}. Got: {}'.format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
