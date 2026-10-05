class Solution(object):
    def answerQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        au=[]
        num=sorted(nums)
        
        for i in range(len(queries)):
            to=0
            co=0
            for j in range(len(num)):
                to+=num[j]
                co+=1
                if to>queries[i]:
                    co-=1
                    break
            au.append(co)
                 
        return au
nums= list(map(int,input('enter nums: ').split()))        
q= list(map(int,input('enter queries: ').split()))  

ou = Solution()
out = ou.answerQueries(nums,q)
print(out)      