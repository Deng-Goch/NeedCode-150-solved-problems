class Solution:
    def isValid(self, s:str):
        le = len(s)
        if le == 0 or le % 2 > 0:
            return False
        else:
            stack = list([])

            for i in s:
                if len(stack) == 0:
                    stack.append(i)
                else:
                    if stack[-1] == '(' and i == ')':
                        stack.pop()
                    elif stack[-1] == '{' and i == '}':
                        stack.pop()
                    elif stack[-1] == '[' and i == ']':
                        stack.pop()
                    else:
                        stack.append(i)

            if len(stack) == 0:
                return True
            else:
                return False


if __name__ == "__main__":

    var = Solution()
    print(var.isValid("{{}}[](([]))"))