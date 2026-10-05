class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Check if the number is negative
        if x < 0:
            return False
        
        # Reverse the number and compare
        self.a = int(str(x)[::-1])  # Reverse the digits
        return x == self.a

# Taking input from the user
num = int(input('Enter a number: '))

# Creating an instance of the Solution class
pal = Solution()

# Checking if the number is a palindrome
if pal.isPalindrome(num):
    print('true')
else:
    print('false')
