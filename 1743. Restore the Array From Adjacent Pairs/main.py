from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        neighbor = {}
        for item in adjacentPairs:
            if not neighbor.get(item[0]):
                neighbor[item[0]] = [item[1]]
            else:
                neighbor[item[0]].append(item[1])

            if not neighbor.get(item[1]):
                neighbor[item[1]] = [item[0]]
            else:
                neighbor[item[1]].append(item[0])

        start = 0
        for key, item in neighbor.items():
            if len(item) == 1:
                start = key
                break

        result, i = [start], 0
        while True:
            key = result[i]
            if len(neighbor[key]) > 0:
                result.append(neighbor[key][0])
                neighbor[neighbor[key][0]].remove(key)
                i += 1
            else:
                break
        return result


Solution().restoreArray([[2, 1], [3, 4], [3, 2]])
