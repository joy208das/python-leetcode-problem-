class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a = []
        
        for i in range(len(nums1)):
            found = False  
            for j in range(len(nums2)):
                
                if nums1[i] == nums2[j]:
                    # Search for the next greater element
                    for k in range(j + 1, len(nums2)):
                        if nums2[k] > nums1[i]:
                            a.append(nums2[k])
                            found = True
                            break
                    if not found:
                        a.append(-1)
                    break  
                
        return a

# Input example
nums1 = list(map(int, input('Enter 1st list (nums1): ').split()))
nums2 = list(map(int, input('Enter 2nd list (nums2): ').split()))

out = Solution()
output = out.nextGreaterElement(nums1, nums2)
print(output)
