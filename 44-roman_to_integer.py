class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        fu = list(map(str, str(s)))
        tu = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000, 
        }
        lu = 0
        i = 0
        while i < len(fu):  
            if i + 1 < len(fu) and fu[i] == "I" and fu[i + 1] == "V":
                lu += 4
                i += 2
            elif i + 1 < len(fu) and fu[i] == "I" and fu[i + 1] == "X":
                lu += 9
                i += 2
            elif i + 1 < len(fu) and fu[i] == "X" and fu[i + 1] == "L":
                lu += 40
                i += 2
            elif i + 1 < len(fu) and fu[i] == "X" and fu[i + 1] == "C":
                lu += 90
                i += 2
            elif i + 1 < len(fu) and fu[i] == "C" and fu[i + 1] == "D":
                lu += 400
                i += 2
            elif i + 1 < len(fu) and fu[i] == "C" and fu[i + 1] == "M":
                lu += 900
                i += 2
            else:
                lu += tu[fu[i]]
                i += 1

        return lu
            
au = input("enter roman op:")

ou = Solution()
out = ou.romanToInt(au)
print(out)
