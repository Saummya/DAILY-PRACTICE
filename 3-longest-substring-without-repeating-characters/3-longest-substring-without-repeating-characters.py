class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        _max = 1
        sub = {s[0]:0}  # index is saved in hashmap for tracking step
        for i in range(1, len(s)):
            if s[i] in sub:
                _max = max(_max, len(sub))
                j = sub[s[i]]
                sub = {k:sub[k] for k in sub if sub[k]>j} 
            sub[s[i]] = i
        return max(_max, len(sub))