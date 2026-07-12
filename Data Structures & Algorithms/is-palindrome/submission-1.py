class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = "".join([ch.lower() for ch in s if ch.isalnum()])
        L = 0
        R = len(ans) - 1

        while L < R:
            if ans[L] != ans[R]:
                return False
            L += 1
            R -= 1
        return True