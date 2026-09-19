# solved, but with extra memory, I need to so this in O(1) space/in-place
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            sv = list()
            tv = list()
            for i in range(0,len(t)):
                sv.append(s[i])
                tv.append(t[i])
            sv.sort()
            tv.sort()
            if sv == tv:
                return True
            else:
                return False


if __name__ == "__main__":
    x = Solution()
    print(x.isAnagram("anagram", "nagaram"))
    print(x.isAnagram("rat", "car"))
    print(x.isAnagram("tes", "stet"))

# ## output:
# ## True
# ## False