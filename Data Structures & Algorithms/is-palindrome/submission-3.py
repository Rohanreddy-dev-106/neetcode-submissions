class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_string=[i.lower() for i in s if i.isalnum()]
        ans = "".join(valid_string)
        L = 0
        R = len(ans) - 1

        while L < R:
            if ans[L] != ans[R]:
                return False
            L += 1
            R -= 1
        return True