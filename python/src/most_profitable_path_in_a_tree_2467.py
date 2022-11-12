"""
Leetcode: https://leetcode.com/problems/most-profitable-path-in-a-tree/
Date: 12-Nov-2022
Author: Ankur Jat (https://www.linkedin.com/in/ankur-jat-41355674/)
"""
from collections import deque, defaultdict


class Solution(object):

    def travrse_bob(self, graph, bob):
        bob_queue = deque([(bob, 0, str(bob))])
        bob_visited = {}
        valid_path = ''
        while bob_queue:
            node, visit_time, path = bob_queue.popleft()
            if node not in bob_visited:
                bob_visited[node] = visit_time
            else:
                continue
            if node == 0:
                valid_path = path
                break
            for child in graph[node].keys():
                if child not in bob_visited:
                    bob_queue.append(
                        (child, visit_time+1, path+"::"+str(child)))
        path = set([int(node.strip())
                    for node in valid_path.split('::') if node.strip()])
        for node in bob_visited.keys():
            if node not in path:
                del bob_visited[node]
        return bob_visited

    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """
        graph = defaultdict(dict)
        for edge in edges:
            graph[edge[0]][edge[1]] = True
            graph[edge[1]][edge[0]] = True

        # Traverse Bob
        bob_visited = self.travrse_bob(graph, bob)

        stack = [(0, 0, 0, None)]
        visited = {}
        cost = set()
        while stack:
            node, visit_time, amount_till_now, parent = stack.pop()
            if node in visited:
                continue
            visited[node] = True
            if node not in bob_visited or bob_visited[node] > visit_time:
                amount_till_now += amount[node]
            elif bob_visited[node] == visit_time:
                amount_till_now += amount[node] / 2
            valid_children = 0
            # print(node, parent, graph[node].keys())
            if len(graph[node].keys()) == 1 and graph[node].keys() == [parent]:
                cost.add(amount_till_now)
            else:
                for child in graph[node].keys():
                    if child not in visited:
                        stack.append(
                            (child, visit_time+1, amount_till_now, node))
        return max(cost)


def test():
    testcases = [
        [[[0, 1], [1, 2], [1, 3], [3, 4]], 3, [-2, 4, 2, -4, 6], 6],
        [[[0, 1]], 1, [-7280, 2350], -7280],
        [[[0, 1], [1, 2], [1, 3], [3, 4]], 3, [-2, 4, 2, -4, 6], 6],
        [[[0, 2], [0, 5], [1, 3], [1, 5], [2, 4]], 4, [
            5018, 8388, 6224, 3466, 3808, 3456], 20328]
    ]
    solution = Solution()
    for index, testcase in enumerate(testcases):
        result = solution.mostProfitablePath(
            testcase[0], testcase[1], testcase[2])
        assert result == testcase[3], "Testcase #{} failed! Expected: {}. Got: {}".format(
            index, testcase[3], result)


if __name__ == "__main__":
    test()
