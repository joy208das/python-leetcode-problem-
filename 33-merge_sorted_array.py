class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i]=nums2[i]
         
        nums1.sort()    
        
        return nums1
        
       
        
nums1=list(map(int,input('enter 1st: ').split()))
m=int(input('enter m: '))
to=list(map(int,input('enter 2nd: ').split()))       
nums2=int(input('enter n:'))

ou=Solution()
out=ou.merge(nums1,m,to,nums2)
print(out)
