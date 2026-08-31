class Solution:
    ## O(1)
    def findMedianSortedArrays(self, nums1:list[int], nums2:list[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        le = len(nums1)

        modu = (le % 2)
        if modu > 0:
            res = round((nums1[le // 2]) / 1, 5)
            return res
        elif modu == 0:
            result2 = round((nums1[le // 2] + nums1[(le - 1) // 2]) / 2, 5)
            return result2


if __name__ == "__main__":
    x = Solution()
    y = [1]
    z = [0,5,7,9,13,17]

    print(x.findMedianSortedArrays(y, z))