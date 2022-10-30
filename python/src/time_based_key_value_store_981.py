"""
Leetcode: https://leetcode.com/problems/time-based-key-value-store/
Date: 4-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class TimeMap(object):

    def __init__(self):
        self.key_store = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if not self.key_store.get(key):
            self.key_store[key] = []
        self.key_store[key].append((timestamp, value))

    def __get_timestamp_value(self, timestamp, timestamps):
        if timestamps[-1][0] <= timestamp:
            return timestamps[-1][1]

        start, end = 0, len(timestamps) - 1
        while start < end:
            mid = (start + end) // 2
            if timestamps[mid][0] < timestamp:
                start = mid + 1
            elif timestamps[mid][0] == timestamp:
                return timestamps[mid][1]
            else:
                end = mid - 1

        if start != 0:
            return timestamps[start-1][1]
        return ""

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if not self.key_store.get(key):
            return ""
        return self.__get_timestamp_value(timestamp, self.key_store[key])


def test():
    testcases = [
        [["TimeMap", "set", "get", "get", "set", "get", "get"],
         [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3],
             ["foo", "bar2", 4], ["foo", 4], ["foo", 5]],
         [None, None, "bar", "bar", None, "bar2", "bar2"]
         ],
        [["TimeMap", "set", "set", "get", "get", "get", "get", "get"],
         [[], ["love", "high", 10], ["love", "low", 20], ["love", 5],
          ["love", 10], ["love", 15], ["love", 20], ["love", 25]],
         [None, None, None, "", "high", "high", "low", "low"]
         ],
        [["TimeMap", "set", "set", "get", "set", "get", "get"],
         [[], ["a", "bar", 1], ["x", "b", 3], ["b", 3],
          ["foo", "bar2", 4], ["foo", 4], ["foo", 5]],
         [None, None, None, "", None, "bar2", "bar2"]
         ],
    ]

    for testcase_index, testcase in enumerate(testcases):
        cache = TimeMap()
        for index, operation in enumerate(testcase[0][1:]):
            if operation == 'set':
                assert cache.set(
                    testcase[1][index+1][0], testcase[1][index+1][1], testcase[1][index+1][2]) == testcase[2][index+1], " Testcase #{testcase_index} failed with inner operation {index}".format(testcase_index=testcase_index, index=index+1)
            elif operation == 'get':
                assert cache.get(
                    testcase[1][index+1][0], testcase[1][index+1][1]) == testcase[2][index+1], " Testcase #{testcase_index} failed with inner operation {index}".format(testcase_index=testcase_index, index=index+1)


if __name__ == "__main__":
    test()
