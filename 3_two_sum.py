## O(n^2)
class Solution(object):
    def twoSum(self, nums:list[int], target:int) -> list[int]:
        if len(nums) < 2:
            return False

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if nums[i] + nums[j] == target:
                        return [i, j]
        return False

if __name__ == "__main__":

    x = Solution()

    print(x.twoSum([], 3))
    ## output: [2,3]

    # x = [0,1,2,3,4]
    # print(x.index(1))

    # x = [3,3,4,7,8]

    # print(list(enumerate(x)))