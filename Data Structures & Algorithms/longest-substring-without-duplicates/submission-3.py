class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(len(s) == 0):
            return 0
        i, j = 0, 0
        obj = {}
        longest = 1
        while j < len(s):
            if(i == j):
                obj[s[i]] = i
                j+=1
            else:
                if(obj.get(s[j]) != None):
                    # duplicate character found, ending the string
                    longest = max(longest, j-i)
                    i=obj.get(s[j])+1
                    j=obj.get(s[j])+1
                    obj={}
                else:
                    obj[s[j]] = j
                    j+=1
        if len(obj.values()) > 0:
            longest = max(longest, j-i)
        
        return longest
            
