class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
            elif interval[0] > newInterval[1]:
                if newInterval not in res:
                    res.append(newInterval)
                res.append(interval)
            else:
                newInterval = [min(interval[0], newInterval[0]), max(interval[1],newInterval[1])]

        if newInterval not in res:
            res.append(newInterval)
        return res
                