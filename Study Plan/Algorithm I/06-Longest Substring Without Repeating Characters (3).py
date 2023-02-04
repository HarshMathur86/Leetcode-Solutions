class Solution:
    def subs_gen(string):
        temp_str = ""
        for char in string:
            if char in temp_str:
                return temp_str
            else:
                temp_str += char
                
        return string
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp_str = ""
        substring = ""
        for i in range(0, len(s)):
            if len(substring) < len(s[i:]):
                temp_str = Solution.subs_gen(s[i:])
                if len(temp_str) > len(substring):
                    substring = temp_str
            else:
                break
            
            
        return len(substring)