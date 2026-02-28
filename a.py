nums = [4,3,2,7,8,2,3,1]

class Solution:
    def findDisappearedNumbers(self, nums) :
        seto = set(nums)
        listo = sorted(seto)
        tempo = 0
        r = []
        for x in listo:
            if x == tempo+1:
                tempo = x
            else:
                # print(tempo)
                while tempo < (x-1):
                    # print(f"{tempo}, {x-1}, {tempo < (x-1)}")
                    tempo = tempo+1
                    r.append(tempo)  
                tempo = tempo+1
        return r 
s = Solution
print(s.findDisappearedNumbers(s, nums))