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


if __name__ == "__main__":
    x = Solution()
    print(x.containsDuplicate([1,2,3,1,4,5]))