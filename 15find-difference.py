class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
      
        result = 0
        for i in s+t:
            result ^= ord(i)
        return chr(result)    
       
        
s=input('enter 1st ele: ')
t=input('enter 2nd ele: ')

out = Solution()

output= out.findTheDifference(s,t)

print(output)

'''In Python, the ord() function returns the Unicode code point (an integer) 
for a given character. This is useful for converting characters to their numeric representation,
which can be especially handy when performing operations like XOR.

Example:
python
Copy code
# Getting the Unicode code point of a character
char = 'a'
code_point = ord(char)
print(code_point)  # Output: 97
In this example, the character 'a' corresponds to the Unicode code point 97.
Similarly, ord('e') would return 101, as e is represented by the code point 101. 
This numeric representation allows for various arithmetic operations to be performed on characters.'''
        