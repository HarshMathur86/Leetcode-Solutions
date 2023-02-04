class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        for w in s1:
            try:
                count_s1[w] += 1
            except:
                count_s1[w] = 1
        
        window = len(s1)
        for i in range(len(s2)-window+1):
            window_str = s2[i:i+window]
            for i in range(len(window_str)):
                if window_str[i] in count_s1.keys():
                    if count_s1[window_str[i]] >= window_str.count(window_str[i]):
                        if i == len(window_str) - 1: 
                            ## for checking if window str is compeletely checked
                            # last char of windows_str
                            return True
                        else:
                            continue
                break
        return False