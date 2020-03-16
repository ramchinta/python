'''Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.'''

class Solution:
    def multiply(self, num1, num2):
        len1 = len(num1)
        len2 = len(num2)
        res = [0]*(len1+len2)
        for i in range(len1-1,-1,-1):
            for j in range(len2-1,-1,-1):
                mul = int(num1[i])*int(num2[j])
                low = i+j+1
                high = i+j
                mul += res[low]
                res[low] = mul%10
                res[high]+=mul//10
        f = False
        result = ''
        for i in range(len(res)):
            if res[i]!=0:
                f = True
            if f:
                result = result + str(res[i])
        return result if result else "0"

print(Solution().multiply("23","34"))
#782