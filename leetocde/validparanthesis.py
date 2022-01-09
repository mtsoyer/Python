class Solution:
    # def isValid(s: str) -> bool:
    #     dicts = {')':'(', ']':'[', '}':'{'}
    #     stack = []
    #     for i in s:
    #         if i in dicts:
    #             print(stack)
    #             if stack!=[] and stack.pop() == dicts[i]:
    #                 print(stack)
    #                 continue
    #             else:
    #                 print("hellop")
    #                 return False
    #         else:
    #             print("i made it ehre")
    #             stack.append(i)
    #     if stack:
    #         return False
    #     else:
    #         return True
    #test for: [] [)] [()]
        def isValid (s: str) -> bool:
            dicts = {
                ")" : "(",
                "}" : "{",
                "]" : "["
            }
            struct = []
            structer = []
            if len(s) < 3:
                    if s[0] in dicts: return False
                    elif s[1] not in dicts: return False
                    elif dicts[s[1]] in s: return True
                    else: return False
            else:
                for num, char in enumerate(s):
                        if s[num] in dicts and struct == []:
                            structer.append(char)
                            continue
                        else:
                            struct.append(char)
                if len(struct) % 2 == 0  and len(structer) % 2 != 0:
                    return True
                else:
                    return False
                
            
            
            
            
        
        print(isValid("[()]"))