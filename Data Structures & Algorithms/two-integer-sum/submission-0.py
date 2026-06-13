class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj = {}
        for i, n in enumerate(nums):
            diff = target-n
            if(obj.get(diff) != None):
                return [obj.get(diff), i]
            else:
                obj[n]=i
