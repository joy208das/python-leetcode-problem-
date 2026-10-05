class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        a = 0
        n = len(arr)
        
        if n % 2 != 0:
            return False  # If the array length is odd, it's impossible to form pairs for all elements.

        for i in range(n):
            if arr[i] is None:
                continue  # Skip if the element is already paired
            for j in range(i + 1, n):
                if arr[j] is None:
                    continue  # Skip if the element is already paired
                if (arr[i] + arr[j]) % k == 0:
                    a += 1
                    arr[i] = None  # Mark the first element as paired
                    arr[j] = None  # Mark the second element as paired
                    break  # Move to the next element after finding a pair

     
        return a == n // 2          
                        
                   
        
        
arr= list(map(int,input('enter el: ').split()))

k =int(input('enter target: '))

out=Solution()

output = out.canArrange(arr,k)

print(output)


'''Understanding the Use of None
Why Use None?
Purpose of None: In Python, None is a special constant that represents the absence of a value or a null value. 
It's often used to signify that a variable doesn't hold any meaningful data.

In Your Code:

Marking Paired Elements: Setting arr[i] and arr[j] to None serves as a marker indicating that these elements have 
already been paired and should not be considered again.
Preventing Reuse: This ensures that each element is used exactly
once in forming pairs, adhering to the problem's constraints.
How None Works in This Context
Initial State: All elements in arr hold their original integer values.

After Pairing:

When a valid pair is found (i.e., (arr[i] + arr[j]) % k == 0), both elements are set to None.
This modification effectively removes these elements from future
pairing considerations without altering the structure of the array.
Subsequent Iterations:

Outer Loop (i): Before attempting to pair arr[i], the code checks if arr[i] is None:. If True, it skips to the next i.
Inner Loop (j): Similarly, if arr[j] is None: ensures that already paired elements are not reconsidered.
Final Check:

By ensuring that the number of valid pairs a matches the expected n // 2,
the code verifies that all elements have been successfully paired without any leftovers.'''
        