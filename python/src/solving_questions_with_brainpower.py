from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        scoreMetrics = [-1] * len(questions)
        scoreMetrics[-1] = questions[-1][0]
        for i in range(len(questions) - 2, -1, -1):
            nextIndex = i + questions[i][1] + 1
            if nextIndex >= len(questions):
                scoreMetrics[i] = max(questions[i][0], scoreMetrics[i+1])
            else:
                scoreMetrics[i] = max(questions[i][0] + scoreMetrics[nextIndex], scoreMetrics[i+1])
        return scoreMetrics[0]

def test():
    testcases = [
        [[[3, 2], [4, 3], [4, 4], [2, 5]], 5],
        [[[1,1],[2,2],[3,3],[4,4],[5,5]], 7],
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.calculate(testcase[0])
        assert result == testcase[1], "Testcase #{} failed! Expected: {}, Got: {}".format(
            index, testcase[1], result)


if __name__ == "__main__":
    test()
