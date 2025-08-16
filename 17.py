"""
class Solution:
    def letterCombinations(self, digits):
        number2alphabet = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                           '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'],
                           '9': ['w', 'x', 'y', 'z']}
        number4digits = len(digits)
        if number4digits == 0:
            result = []
            return result
        elif number4digits == 1 and '1' not in digits:
            result = [f"{a}" for a in number2alphabet[digits[0]]]
            return result
        elif number4digits == 2 and '1' not in digits:
            result = [f"{a}{b}" for a in number2alphabet[digits[0]] for b in number2alphabet[digits[1]]]
            return result
        elif number4digits == 3 and '1' not in digits:
            result = [f"{a}{b}{c}" for a in number2alphabet[digits[0]] for b in number2alphabet[digits[1]] for c in number2alphabet[digits[2]]]
            return result
        elif number4digits == 4 and '1' not in digits:
            result = [f"{a}{b}{c}{d}" for a in number2alphabet[digits[0]] for b in number2alphabet[digits[1]] for c in number2alphabet[digits[2]] for d in number2alphabet[digits[3]]]
            return result
        else:
            print("number of digits unexpected.")
"""


def subsets(nums):
    result = []  # 最终结果

    def backtrack(start, path):  # 定义回溯函数
        print("under backtrack")
        print(start)
        print(path)
        result.append(path[:])  # 将当前的已选食材放入结果中（这个已经是一个完整的套餐）

        for i in range(start, len(nums)):  # 从第一个食材开始，逐个选择
            print(start)
            print(path)
            path.append(nums[i])  # 选择一个食材
            print(start)
            print(path)
            backtrack(i + 1, path)  # 递归调用，继续选择下一个食材
            print(start)
            print(path)
            path.pop()  # 撤销选择，回退到上一个状态
            print(start)
            print(path)

    backtrack(0, [])  # 从第一个食材开始，空菜单
    print(result)
    return result  # 返回所有可能的套餐组合


subsets([1, 2, 3])
