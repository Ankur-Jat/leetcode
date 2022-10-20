"""
Leetcode: https://leetcode.com/problems/top-k-frequent-words/
Date: 19-Oct-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
import heapq


class Word(object):
    def __init__(self, word):
        self.word = word
        self.count = 1

    def __lt__(self, other):
        if self.count < other.count:
            return True
        if self.count == other.count:
            return self.word > other.word
        return False


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        words_dict = {}
        word_list = []
        for word in words:
            if word not in words_dict:
                word_obj = Word(word)
                words_dict[word] = word_obj
                word_list.append(word_obj)
            else:
                words_dict[word].count += 1
        kheap = word_list[:k][:]
        heapq.heapify(kheap)
        for word in word_list[k:]:
            heapq.heappushpop(kheap, word)

        result = []
        while kheap:
            result.append(heapq.heappop(kheap).word)
        return result[::-1]


def test():
    solution = Solution()
    testcases = [
        [["i", "love", "leetcode", "i", "love", "coding"], 2, ["i", "love"]],
        [["the", "day", "is", "sunny", "the", "the", "the",
            "sunny", "is", "is"], 4, ["the", "is", "sunny", "day"]],
        [["glarko", "zlfiwwb", "nsfspyox", "pwqvwmlgri", "qggx", "qrkgmliewc", "zskaqzwo", "zskaqzwo", "ijy", "htpvnmozay", "jqrlad", "ccjel", "qrkgmliewc", "qkjzgws", "fqizrrnmif", "jqrlad", "nbuorw", "qrkgmliewc", "htpvnmozay", "nftk", "glarko", "hdemkfr", "axyak", "hdemkfr", "nsfspyox", "nsfspyox", "qrkgmliewc", "nftk", "nftk", "ccjel", "qrkgmliewc", "ocgjsu", "ijy", "glarko", "nbuorw", "nsfspyox", "qkjzgws", "qkjzgws", "fqizrrnmif", "pwqvwmlgri", "nftk", "qrkgmliewc", "jqrlad", "nftk", "zskaqzwo", "glarko", "nsfspyox", "zlfiwwb", "hwlvqgkdbo", "htpvnmozay", "nsfspyox", "zskaqzwo", "htpvnmozay", "zskaqzwo", "nbuorw", "qkjzgws", "zlfiwwb", "pwqvwmlgri", "zskaqzwo", "qengse", "glarko", "qkjzgws", "pwqvwmlgri", "fqizrrnmif",
            "nbuorw", "nftk", "ijy", "hdemkfr", "nftk", "qkjzgws", "jqrlad", "nftk", "ccjel", "qggx", "ijy", "qengse", "nftk", "htpvnmozay", "qengse", "eonrg", "qengse", "fqizrrnmif", "hwlvqgkdbo", "qengse", "qengse", "qggx", "qkjzgws", "qggx", "pwqvwmlgri", "htpvnmozay", "qrkgmliewc", "qengse", "fqizrrnmif", "qkjzgws", "qengse", "nftk", "htpvnmozay", "qggx", "zlfiwwb", "bwp", "ocgjsu", "qrkgmliewc", "ccjel", "hdemkfr", "nsfspyox", "hdemkfr", "qggx", "zlfiwwb", "nsfspyox", "ijy", "qkjzgws", "fqizrrnmif", "qkjzgws", "qrkgmliewc", "glarko", "hdemkfr", "pwqvwmlgri"], 14, ["nftk", "qkjzgws", "qrkgmliewc", "nsfspyox", "qengse", "htpvnmozay", "fqizrrnmif", "glarko", "hdemkfr", "pwqvwmlgri", "qggx", "zskaqzwo", "ijy", "zlfiwwb"]]
    ]
    for index, testcase in enumerate(testcases):
        assert solution.topKFrequent(
            testcase[0], testcase[1]) == testcase[2], "Testcase #{} failed".format(index)


if __name__ == "__main__":
    test()
