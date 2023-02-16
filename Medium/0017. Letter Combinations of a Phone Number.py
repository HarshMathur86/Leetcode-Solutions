class Solution:
    letters = {
        "2":"abc",
        "3":"def",
        "4":"ghi",
        "5":"jkl",
        "6":"mno",
        "7":"pqrs",
        "8":"tuv",
        "9":"wxyz"
    }
    combinations = []
    
    def comb_calculator(self, comb, digits):
        #print("Got --> ", digits, ", current combination --> ", comb)
        if digits == "":
            Solution.combinations.append(comb)
        else:
            for let in Solution.letters[digits[0]]:
                self.comb_calculator(comb+let, digits[1:])

    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        Solution.combinations = []
        self.comb_calculator("", digits)
        return Solution.combinations