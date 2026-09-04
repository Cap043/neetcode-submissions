class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # result=[]
        # right=0
        # for i in range(len(temperatures)):
        #     flag=False
        #     for right in range (i+1,len(temperatures)):
        #         if temperatures[right]>temperatures[i]:
        #             result.append(right-i)
        #             flag=True
        #             break
        #     if not flag:
        #         result.append(0)

        # return result
        result=[0]* len(temperatures)
        stack=[]
        for i,n in enumerate(temperatures):
            while stack and stack[-1][0]<n:
                temp,index= stack.pop()
                result[index]=i-index


            stack.append([n,i])
        return result
