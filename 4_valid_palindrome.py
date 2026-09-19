## O(n) where n = the length of the string s.
class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = list([])
        for i in range(0, len(s)):
            if ord(s[i]) > 47 and ord(s[i]) < 58:
                arr.append(s[i])
            elif ord(s[i]) > 64 and ord(s[i]) < 91:
                arr.append(s[i].lower())
            elif ord(s[i]) > 96 and ord(s[i]) < 123:
                arr.append(s[i])
            else:
                continue
        
        l = 0
        r = (len(arr)-1)
        iters = (len(arr)//2)

        while iters > 0:
            if arr[l] == arr[r]:
                l += 1
                r -= 1
            else:
                return False
            iters -= 1
        return True


if __name__ == "__main__":
    x = Solution()
    y = "A man, a plan, a canal: Panama"
    print(x.isPalindrome(y))
