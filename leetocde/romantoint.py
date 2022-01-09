# class Solution(object):
#     def romanToInt( s):
#         """
#         :type s: str
#         :rtype: int
#         """
#         mydict = {'I':1, 'V':5, 'X':10 , 'L':50, 'C':100, 'D':500, 'M':1000}
#         finalnum = 0
#         for i in range(len(s)-1):
#             if mydict[s[i]] < mydict[s[i+1]]:
#                 finalnum -= mydict[s[i]]
#             else:
#                 finalnum += mydict[s[i]]
#         finalnum += mydict[s[-1]]
#         return finalnum


class Solution:
    def romanToInt( s: str) -> int:
        
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sub_cases = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
        
        result = 0
        prev_letter = ''
        
        for char in s:
            if prev_letter + char in sub_cases:
                result += roman_dict[char]-2*roman_dict[prev_letter]
            else:
                result += roman_dict[char]
        
            prev_letter = char
        return result


    print(romanToInt("MV"))
