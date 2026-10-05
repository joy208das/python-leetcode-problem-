class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        # a= flowerbed.count(0)
        # if a==((2*n)+1):
        #     return True
        # else:
        #     return False
        
        a=len(flowerbed)
        if n==0:
            return True
        for i in range(len(flowerbed)):
          if flowerbed[i]==0 and (i==0 or flowerbed[i-1]==0) and (i==a-1 or flowerbed[i+1]==0):
              flowerbed[i]=1
              n-=1
              if n==0:
                return True
        return False
                     
flowerbed = list(map(int,input('enter flowers: ').split()))
n = int(input())

out  = Solution()
output=out.canPlaceFlowers(flowerbed,n)
print(output)      