class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        lower_s = s.lower()
        print(lower_s)
        if i == j:
            return True
        while i < j:
            while i < j and not lower_s[i].isalnum():
                i += 1
            while i< j and not lower_s[j].isalnum():
                j -= 1

            if lower_s[i] != lower_s[j]:
                return False
            
            i += 1
            j -= 1

        return True