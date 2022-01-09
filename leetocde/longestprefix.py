#class Solution:
    # def longpref(strs: list[str]):
    #     """finds the longest prefix in a list. if non are there, it returns nothing
    #     """
    #     flag = False
    #     stringbuilder = ""
    #     temp = list(sorted(strs, key=len))
    #     word = temp[0]
    #     for char in range(0, len(word)):
    #         for words in strs:
    #             if word[char] == words[char]:
    #                 flag = True
    #             else:
    #                 flag = False
    #                 break
    #         if flag:
    #             stringbuilder += word[char]
    #         else:
    #             break
    #     return stringbuilder
    
    # def longestCommonPrefix(strs):
    #     prefix=""
    #     if len(strs)==0: return prefix
        
    #     for i in range(len(min(strs))):
    #         c=strs[0][i]
    #         if all(a[i]==c for a in strs):
    #             prefix+=c
    #         else:
    #             break
    #     return prefix
    #     if not strs: return ""
    #     if len(strs) == 1: return strs[0]
        
    #     strs.sort()
    #     p = ""
    #     for x, y in zip(strs[0], strs[-1]):
    #         if x == y: p+=x
    #         else: break
    #     return p
    
    # print(longestCommonPrefix(["reflower","flow","flight"]))
    
        
        
        
    