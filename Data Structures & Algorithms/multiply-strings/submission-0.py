# Use dict to convert string to number
# 10^{i - 1}
# Once you get digits, just multiply
STR_TO_DIGIT = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "0": 0
}

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convertToInt(num: str) -> int:
            res = 0
            power = len(num) - 1
            for char in num:
                res += STR_TO_DIGIT[char] * (10 ** power)
                power -= 1
            # print(res)
            return res
        
        return str(convertToInt(num1) * convertToInt(num2))