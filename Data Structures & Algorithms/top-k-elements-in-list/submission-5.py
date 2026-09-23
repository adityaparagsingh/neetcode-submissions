from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        bucket = [0]*(n+1)     #using bucket sort (created an array of length n+1 filled with zeroes)
        for key,val in counter.items():
            if bucket[val] == 0:
                bucket[val] = [key]
            else:
                bucket[val].append(key)
        ret = []
        for i in range(n,-1,-1):
            if bucket[i]!=0:
                ret.extend(bucket[i])
            if len(ret) == k:
                break
        return ret