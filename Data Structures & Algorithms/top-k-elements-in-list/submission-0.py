class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums.sort()
        # sets = set(nums)
        # # x=0
        # arr = []
        # # while x!=k:
        # for i in range(len(nums)):
        #     count = 0
        #     while nums[i]==nums[count]:
        #         count+=1
        #         arr.append(count)
        # arr.sort(reverse = True)
        nums.sort()
        freq = []
        i = 0
        while i < len(nums):
            count = 1
            while i + count < len(nums) and nums[i] == nums[i + count]:
                count += 1
            freq.append((count, nums[i]))
            i += count
        freq.sort(reverse=True)
        return [num for count, num in freq[:k]]