class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_arr = []
        for ind, v in enumerate(nums):
            if(ind > 0 and nums[ind-1] == v): # handling the duplicates
                continue
            
            i,j = ind+1, len(nums)-1
            while i<j:
                s = v + nums[i] + nums[j]
                if(s == 0):
                    final_arr.append([v, nums[i], nums[j]])
                    i+=1
                    if(i > 0 and nums[i] == nums[i-1]):
                        while nums[i] == nums[i-1] and i<j:
                            i+=1
                elif(s < 0):
                    i+=1
                else:
                    j-=1

        return final_arr
            



        
                