# class Solution(object):
#     def singleNumber(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         x= len(nums)
        
#         if len(nums)==1:
#                     return nums[0]
#         else:
#             for i in range(0,x):
#                 for j in range(i+1,x):
#                         if nums[i]!=nums[j]:
#                             return nums[i]
            
        
# nums = list(map(int,input('enter elements: ').split()))        

# p= Solution()

# a=p.singleNumber(nums)
# print(a)


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num  # XOR operation
        return result

nums = list(map(int, input('Enter elements: ').split()))

p = Solution()

a = p.singleNumber(nums)
print(a)

'''
1. Understanding Binary Numbers
Before diving into XOR, it's essential to understand binary numbers because XOR operates at the bit level.

Binary System: A base-2 numeral system that uses two symbols: 0 and 1.
Bits: The smallest unit of data in computing, representing a single binary digit (0 or 1).
Example:

Decimal 2 in binary: 10
Decimal 3 in binary: 11
Decimal 4 in binary: 100
2. What is XOR?
XOR stands for "Exclusive OR". It's a bitwise operator, meaning it works on individual bits of binary numbers.

Purpose: Compare two bits and return 1 if the bits are different, and 0 if they are the same.
3. XOR Truth Table
A truth table shows the output of XOR for all possible input combinations.

A	B	A XOR B
0	0	0
0	1	1
1	0	1
1	1	0
Interpretation:

If both bits are the same (0 and 0 or 1 and 1), the result is 0.
If bits are different (0 and 1 or 1 and 0), the result is 1.
4. Bitwise XOR Operation
When you apply XOR to two numbers, the operation is performed bit by bit.

Example: Let's XOR 5 and 3.

Convert to Binary:

5 in binary: 101
3 in binary: 011
Align the Bits:

markdown
Copy code
  1 0 1  (5)
XOR
  0 1 1  (3)
---------
  1 1 0  (Result)
Compute XOR for Each Bit:

First Bit (from the right): 1 XOR 1 = 0
Second Bit: 0 XOR 1 = 1
Third Bit: 1 XOR 0 = 1
Combine the Result: 110 in binary is 6 in decimal.

So, 5 XOR 3 = 6.

5. Why Use XOR in Your Code?
In your problem, you need to find the unique element in an array where every other element appears twice. Here's why XOR is perfect for this:

Duplicate Cancellation: XOR-ing two identical numbers results in 0 (A XOR A = 0).
Unique Preservation: XOR-ing 0 with a number keeps the number unchanged (0 XOR B = B).
Combining Both: When you XOR all numbers in the array, duplicates cancel out, leaving the unique number.
Example:

Array: [2, 3, 2, 4, 4]
XOR all elements: 2 XOR 3 XOR 2 XOR 4 XOR 4
Calculation:
2 XOR 3 = 1
1 XOR 2 = 3
3 XOR 4 = 7
7 XOR 4 = 3
Result: 3 (the unique number)
6. Step-by-Step Example
Let's walk through how the XOR operation works in your code with a concrete example.

Given Array: [2, 3, 2, 4, 4]

Goal: Find the unique number (3 in this case).

Code Snippet:

python
Copy code
class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:
            result ^= num  # XOR operation
        return result

nums = [2, 3, 2, 4, 4]
p = Solution()
a = p.singleNumber(nums)
print(a)  # Output: 3
Step-by-Step XOR Operations:

Initialization:

makefile
Copy code
result = 0
First Iteration (num = 2):

makefile
Copy code
result = 0 XOR 2 = 2
Binary: 000 XOR 010 = 010 (which is 2)
Second Iteration (num = 3):

makefile
Copy code
result = 2 XOR 3 = 1
Binary: 010 XOR 011 = 001 (which is 1)
Third Iteration (num = 2):

makefile
Copy code
result = 1 XOR 2 = 3
Binary: 001 XOR 010 = 011 (which is 3)
Fourth Iteration (num = 4):

makefile
Copy code
result = 3 XOR 4 = 7
Binary: 011 XOR 100 = 111 (which is 7)
Fifth Iteration (num = 4):

makefile
Copy code
result = 7 XOR 4 = 3
Binary: 111 XOR 100 = 011 (which is 3)
Final Result:

makefile
Copy code
result = 3
Explanation:

Duplicates Canceled Out: Both 2s and both 4s cancel each other out.
Unique Number Left: 3 remains as the unique number.
7. Visualizing XOR
Sometimes, visual aids can make things clearer. Let’s visualize the XOR process with a smaller example.

Example: XOR 1 and 4.

Convert to Binary:

1 in binary: 001
4 in binary: 100
Apply XOR:

markdown
Copy code
  0 0 1
XOR
  1 0 0
---------
  1 0 1  (which is 5)
Result: 5

Explanation:

Bit 1: 1 XOR 0 = 1
Bit 2: 0 XOR 0 = 0
Bit 3: 0 XOR 1 = 1
So, 1 XOR 4 = 5.

8. Summary
Binary Basics: Understanding binary (base-2) numbers is crucial since XOR operates at the bit level.
XOR Operation: Compares two bits and returns 1 if they are different, 0 if they are the same.
Bitwise Application: When applied to whole numbers, XOR processes each corresponding pair of bits.
Duplicate Cancellation: In your problem, XOR effectively cancels out duplicate numbers, leaving the unique one.
Efficiency: Using XOR allows you to solve the problem in linear time O(n) with constant space O(1).


'''