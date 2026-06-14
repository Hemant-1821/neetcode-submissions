class Solution:
    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "0"
        enc_str = ""
        for i in strs:
            enc_str += str(len(i))+'#'+i
        print(enc_str)
        return enc_str

    def decode(self, s: str) -> List[str]:
        dec_arr = []
        if(s == "0"):
            return dec_arr
        i = 0
        len_str = ""
        while i < len(s):
            if(s[i] == '#'):
                dec_arr.append(s[i+1:i+1+int(len_str)])
                i += int(len_str)+1
                len_str = ""
                continue
            if(s[i].isnumeric()):
                len_str += s[i]
                i+=1

        return dec_arr
            

            
