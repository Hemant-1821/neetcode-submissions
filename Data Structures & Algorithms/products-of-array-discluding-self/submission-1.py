from functools import reduce

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [None for i in range(len(nums))]
        post = pre.copy()
        
        #finding pre multiplications
        pre[0] = 1
        for i in range(1, len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
        #finding post multiplications
        post[-1] = 1
        for i in range(len(post)-2, -1, -1):
            post[i] = post[i+1]*nums[i+1]

        prod_arr = []
        for i,v in enumerate(pre):
            prod_arr.append(v*post[i])

        return prod_arr