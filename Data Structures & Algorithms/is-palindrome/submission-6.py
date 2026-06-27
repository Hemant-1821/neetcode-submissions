class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        lower_s = s.lower()
        print(lower_s)
        if i == j:
            return True
        while i <= (len(s)-1)//2:
            print("For ", lower_s[i], i)
            while not lower_s[i].isalnum() and i <= (len(s)-1)//2:
                print(lower_s[i])
                i += 1
            while not lower_s[j].isalnum() and j >= (len(s)-1)//2:
                j -= 1
            if i > j:
                break
            if lower_s[i] != lower_s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True