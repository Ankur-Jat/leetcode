"""
Leetcode: https://leetcode.com/problems/minimum-genetic-mutation/
Date: 2-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        if end not in bank:
            return -1
        if start == end:
            return 0

        def get_possible_next_seq(current_start, current_bank):
            diff1_next = []
            for index in range(len(current_bank)):
                seq = current_bank[index]
                diff = 0
                for inner_index in range(8):
                    if current_start[inner_index] != seq[inner_index]:
                        diff += 1
                        if diff > 1:
                            break
                if diff == 1:
                    diff1_next.append((seq, index))
            return diff1_next

        diff1_next = get_possible_next_seq(start, bank)
        if not diff1_next:
            return -1

        final_result = []
        for next_possible_seq, index in diff1_next:
            if next_possible_seq == end:
                return 1
            result = self.minMutation(
                next_possible_seq, end, bank[0:index] + bank[index+1:])
            if result != -1:
                final_result.append(1+result)
        if not final_result:
            return -1
        return min(final_result)


def test():
    testcases = [
        ["AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1],
        ["AACCGGTT", "AAACGGTA", ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"], 4],
        ["AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"], 2],
        ["AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"], 3],
        ["AACCTTGG", "AATTCCGG", ["AATTCCGG", "AACCTGGG", "AACCCCGG", "AACCTACC"], -1],
        ["AAAACCCC", "CCCCCCCC", ["AAAACCCA", "AAACCCCA", "AACCCCCA",
                                  "AACCCCCC", "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"], 4]
    ]

    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.minMutation(
            testcase[0], testcase[1], testcase[2]) == testcase[3], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
