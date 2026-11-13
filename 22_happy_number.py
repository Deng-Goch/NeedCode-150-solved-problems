class Solution:
    def isHappy(self, n: int) -> bool:

        def loop(n):
            casted = str(n)
            sum = 0

            for inte in casted:
                sum += (int(inte) ** 2)

            return sum

        cached = set()

        while True:
            iter = loop(n)
            if iter not in cached:
                cached.add(iter)
                if iter == 1:
                    return True
                else:
                    n = iter
            else:
                return False
                

if __name__ == "__main__":
    var = Solution()

    print(var.isHappy(7))