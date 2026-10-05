class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        au = [char for char in order if char in s]
        for i in s:
          if i not in au:
              au.append(i)
              
        return ''.join(au)   
    
        
order = input()
s = input()
out = Solution()
put = out.customSortString(order,s)

print(put)        