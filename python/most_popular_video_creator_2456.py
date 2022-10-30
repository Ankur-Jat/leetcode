"""
Leetcode: https://leetcode.com/problems/most-popular-video-creator/
Date: 28-oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""


class Solution(object):
    def mostPopularCreator(self, creators, ids, views):
        """
        :type creators: List[str]
        :type ids: List[str]
        :type views: List[int]
        :rtype: List[List[str]]
        """
        creator_dict = {}
        max_video_count = float('-inf')
        for index in range(len(creators)):
            creator = creators[index]
            if creator not in creator_dict:
                creator_dict[creator] = {
                    'video_count': 0,
                    "highest_viewed_video_count": float('-inf'),
                    "video_id": float('inf')
                }
            creator_data = creator_dict[creator]
            creator_data["video_count"] += views[index]
            max_video_count = max(max_video_count, creator_data["video_count"])
            if views[index] > creator_data["highest_viewed_video_count"]:
                creator_data["highest_viewed_video_count"] = views[index]
                creator_data["video_id"] = ids[index]
            elif views[index] == creator_data["highest_viewed_video_count"] and creator_data["video_id"] > ids[index]:
                creator_data["video_id"] = ids[index]

        result = []
        for creator, data in creator_dict.items():
            if data["video_count"] == max_video_count:
                result.append([creator, data['video_id']])
        return result

def test():
    testcases = [
        [
            ["alice", "bob", "alice", "chris"],
            ["one", "two", "three", "four"],
            [5, 10, 5, 4],
            [["bob", "two"], ["alice", "one"]]
        ],
        [
            ["alice", "alice", "alice"],
            ["a", "b", "c"],
            [1, 2, 2],
            [["alice", "b"]]
        ]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        assert solution.mostPopularCreator(testcase[0], testcase[1], testcase[2]) == testcase[3], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
