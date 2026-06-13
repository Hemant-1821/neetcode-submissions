class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        dup = False
        for i in nums:
            if(not dic.get(i)):
                dic[i] = True
            else:
                dup = True
                break
        return dup

        