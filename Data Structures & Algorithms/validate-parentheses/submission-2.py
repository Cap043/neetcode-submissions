class Solution:
    def isValid(self, s: str) -> bool:
        control=[]
        bracketDict={")":"(", "}":"{", "]":"["}
        for c in s:
            if c in bracketDict:
                if control and (control[-1]==bracketDict[c]):
                    control.pop()
                else:return False
            else: control.append(c)
        return not len(control)

                    
                

        
    

            
            
            

