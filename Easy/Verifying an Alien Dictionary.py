""" Que ---> 
953
"""

# Solution 
class Solution:
    order_char = {}
        
    def isFirstGreater(f, l):
        if len(f)>len(l):
            if f.startswith(l):
                return True
        else:
            if l.startswith(f):
                return False
        
        for i in range(len(f)):
            if Solution.order_char[f[i]] < Solution.order_char[l[i]]:
                return False
            elif Solution.order_char[f[i]] == Solution.order_char[l[i]]:
                continue
            else:
                return True
    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        Solution.order_char = {}
        for i in range(len(order)):
            Solution.order_char[order[i]] = i+1

        for i in range(len(words)-1):
            first = words[i]
            last = words[i+1]
            if Solution.isFirstGreater(first, last):
                return False
        return True
        