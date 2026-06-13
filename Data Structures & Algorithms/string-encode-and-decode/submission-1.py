class Solution:
    def remove_zeros(self, num_str):
        ind = 0
        for i, a in enumerate(num_str):
            if(int(a)>0):
                ind = i
                break
        return int(num_str[ind:])
    def encode(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return '0'
        enc_arr = []
        for i in strs:
            int_str = ""
            for alpha in i:
                int_str += str(ord(alpha)).zfill(3)
            enc_arr.append(int_str)
        return ";".join(enc_arr)

    def decode(self, s: str) -> List[str]:
        if(s == '0'):
            return []
        split_arr = s.split(";")
        final_arr = []
        for i in split_arr:
            curr_str = ""
            for j in range(0, len(i), 3):
                num = self.remove_zeros(i[j:j+3])
                curr_str += chr(num)
            final_arr.append(curr_str)
        return final_arr
