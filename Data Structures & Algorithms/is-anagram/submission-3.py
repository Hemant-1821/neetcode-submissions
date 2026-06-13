class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) == len(t)):
            obj = {}
            for i in s:
                if(obj.get(i)):
                    obj[i] += 1
                else:
                    obj[i] = 1
            for j in t:
                if(obj.get(j) and obj[j] > 0):
                    obj[j] -= 1
                else:
                    return False
            return True
        else:
            return False