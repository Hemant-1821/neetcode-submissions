class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        hash_map = {}
        for i in nums:
            hash_map[i] = True
        print(hash_map)
        longest_count = 1
        for i in nums:
            temp_count = 1
            num = i
            while True:

                if(hash_map.get(num+1)):
                    temp_count += 1
                    num += 1
                else:
                    break
            if(temp_count > longest_count):
                longest_count = temp_count
        
        return longest_count
        