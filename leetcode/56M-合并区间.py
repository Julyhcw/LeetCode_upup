class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n < 1: return
        # intervals.sort()
        # ans = [intervals[0]]
        # for i in range(1,n):
        #     if intervals[i][0] <= ans[-1][1]:
        #         ans[-1][1] = max(intervals[i][1],ans[-1][1])
        #         #ans.append([ans[-1][0],max(intervals[i][1],ans[-1][1])])
        #     else:
        #         ans.append(intervals[i])
        # return ans
        
        i, j = 0, 1
        intervals.sort()
        while j < n :
            #print(intervals)
            if i < n - 1 and intervals[i][1] >= intervals[i + 1][0]:
                tmp = [intervals[i][0], max(intervals[i + 1][1], intervals[i][1])]
                intervals.remove(intervals[i])
                intervals.remove(intervals[i])
                intervals.insert(i, tmp)
                j += 1
            else:
                i += 1
                j += 1
        return intervals
            