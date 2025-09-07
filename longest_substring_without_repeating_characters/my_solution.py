class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        length = longest = 0
        for i, c in enumerate(s):
            if c not in seen:
                length += 1
                seen.add(c)
            else:
                addlater = [c]
                i -= 1
                while c != s[i]:
                    addlater.append(s[i])
                    i -= 1
                
                seen.clear()
                seen.update(addlater)
                length = len(addlater)
              
            if length > longest:
                longest = length
        return longest