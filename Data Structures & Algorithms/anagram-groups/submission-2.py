class Solution:
    def check_anagram(self, s, t):
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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        obj = {}
        ana = []
        for i in strs:
            if(obj.get(len(i))):
                obj[len(i)] = obj[len(i)] + [i]
            else:
                obj[len(i)] = [i]

        for i, v in obj.items():
            arr = v
            while len(arr) > 0:
                if(len(arr) == 1):
                    ana.append(arr)
                    break
                ele = arr.pop(0)
                temp = [ele]
                for index, value in enumerate(arr[:]):
                    if(self.check_anagram(ele, value)):
                        temp.append(value)
                        arr.remove(value)

                ana.append(temp)
        return ana



