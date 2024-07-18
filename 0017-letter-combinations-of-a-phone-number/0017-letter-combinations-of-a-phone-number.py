class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtrack(index, current_combination):
            if index == len(digits):
                result.append(current_combination)
                return
            
            for letter in digit_to_letters[digits[index]]:
                backtrack(index + 1, current_combination + letter)
        
        result = []
        backtrack(0, "")
        return result