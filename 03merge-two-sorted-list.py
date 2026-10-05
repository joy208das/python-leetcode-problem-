class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        return list1+list2
        
        
list1 = list(map(int, input("Enter the numbers in the array, separated by spaces: ").split()))    
list2 = list(map(int, input("Enter the numbers in the array, separated by spaces: ").split()))

p =Solution()

print(p.mergeTwoLists(list1,list2) )
