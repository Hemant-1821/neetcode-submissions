class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums) == 0):
            return 0
        hash_map = {}
        for i in nums:
            hash_map[i] = True

        longest_count = 1
        hash_map_cons = {}
        for i in nums:
            temp_count = 1
            num = i
            while True:
                if(hash_map_cons.get(num+1)):
                    temp_count += hash_map_cons.get(num+1)
                    num += hash_map_cons.get(num+1)
                elif(hash_map.get(num+1)):
                    temp_count += 1
                    num += 1
                else:
                    break
            hash_map_cons[i] = temp_count
            if(temp_count > longest_count):
                longest_count = temp_count
        
        return longest_count
        