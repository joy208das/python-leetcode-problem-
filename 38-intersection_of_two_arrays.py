class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a=set()
        for i in nums1:
            if i in nums2:
                a.add(i)
                
        return list(a)        
        
        
nums1 = list(map(int,input('enter set1:').split()))
nums2 = list(map(int,input('enter 0et2s:').split()))

ou =Solution()
out= ou.intersection(nums1,nums2)
print(out)               