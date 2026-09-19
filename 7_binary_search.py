## iterative binary search - O (log2 N)
class Solution:
    def BinSearch(self, nums:list, target:int):
        left = 0
        right = (len(nums)-1)

        while left <= right:
            mid = ((left + right) // 2)

            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = (mid - 1)
            else:
                left = (mid + 1)
        return (-1)


if __name__ == "__main__":

    # print(Solution.binSearch([1,2,3,4,5,6,7,8,9,0], 20))
    x = Solution()
    print(x.BinSearch([-1,0,12,3,9,5,9,12], 100))