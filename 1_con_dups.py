## Solution 1
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        def bin_search(arr:list, target):
            n = len(arr)
            l = 0
            r = (n -1)
            arr.sort()
            while l <= r:
                m = (l + ((r - l) // 2))
                if arr[m] == target:
                    return True
                elif target < arr[m]:
                    r = (m - 1)
                else:
                    l = (m + 1)
            return False
        
        arr = list()
        for i in range(0,len(nums)):
            if bin_search(arr,nums[i]) == True:
                return True
            else:
                arr.append(nums[i])
        return False




# valid solution, but not effective.
# I need to optimize it.
# wasn't able to solve the problem due to time limit exceeding.

## Solution 2
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort()
        for i in range(0, len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False




# valid solution, but not effective.
# I need to optimize it.
# Was able to solve the problem, but in a very big time complexity.

## kind of optimized solution, O(n) time, O(n) space
## Solution 3
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        se = set()
        for i in nums:
            if i not in se:
                se.add(i)
            else:
                return True
        return False



## Solution 4
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else:
            return True

if __name__ == "__main__":
    x = Solution()
    print(x.containsDuplicate([1,2,3,4,5]))