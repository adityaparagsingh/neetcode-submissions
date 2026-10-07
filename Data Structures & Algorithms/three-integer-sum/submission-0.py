class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        lst = set()
        nums.sort()
        n = len(nums)

        for i in range(n):
            j,k = i+1,n-1

            while j<k:
                if nums[j]+nums[k] < -(nums[i]):
                    j+=1
                
                elif nums[j]+nums[k] > -(nums[i]):
                    k-=1
                
                else:
                    lst.add((nums[i],nums[j],nums[k]))                
                    j += 1
                    k -= 1
        return [list(t) for t in lst]