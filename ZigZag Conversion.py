'''The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I'''


class Solution:
    def convert(s, numRows):
        if s == None:
            return s
        if numRows == 0:
            return s
        if numRows == 1:
            return s
        rstr = ''
        for i in range(numRows):
            if i == 0:
                rstr = rstr + s[::numRows + (numRows - 2)]
            elif i == numRows - 1:
                rstr = rstr + s[i::numRows + (numRows - 2)]
            else:
                spacea = 2 * (numRows - i - 1)
                spaceb = 2 * i
                counter = 0
                j = i
                while j < len(s):
                    rstr = rstr + s[j]
                    if counter % 2 == 0:
                        j = j + spacea
                    else:
                        j = j + spaceb
                    counter = counter + 1

        return rstr

print(Solution.convert('Paypalishiring',4))
#Pinalsigyahrpi