class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        output_list=[-1]*len(temperatures)
        for t in range(len(temperatures)-1 ,-1 ,-1):
                while stack and temperatures[t]>=temperatures[stack[-1]]:
                      stack.pop()
                if not stack:
                   output_list[t]=0 
                else:
                    output_list[t]= stack[-1] - t
                stack.append(t)

        return  output_list



        