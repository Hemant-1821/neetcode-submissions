class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj = {}
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            obj[i] = obj.get(i, 0) + 1
        
        for n, v in obj.items():
            freq[v].append(n)

        final_arr = []
        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                final_arr.append(j)
                if len(final_arr) == k:
                    return final_arr