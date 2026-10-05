'''Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.'''

class Solution:
    def sortPeople(self,names,heights):
        # Zip heights and names to tuples where each tuple is (heights[i], names[i])
        # Then sort based on the heights, and with reverse (descending)
        sorted_heights = sorted(zip(heights, names), reverse=True)
        # Append the names in the sorted order (2nd element of each tuple)
        res = [name for height,name in sorted_heights]
        return res
        

names = list(map(str,input('enter names: ').split()))

heights = list(map(int,input('enter heights: ').split()))

out = Solution()
output = out.sortPeople(names,heights)

print(output)