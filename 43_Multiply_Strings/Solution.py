
# -*- coding:utf-8 -*-
__author__ = "ethan"

#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

#Note:
#The length of both num1 and num2 is < 110.
#Both num1 and num2 contains only digits 0-9.
#Both num1 and num2 does not contain any leading zero.
#You must not use any built-in BigInteger library or convert the inputs to integer directly.

import functools

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        len1 = len(num1)
        len2 = len(num2)
        if len1 < len2 or (len1 == len2 and num1 < num2):
            num1, num2 = num2, num1
            len1, len2 = len2, len1
        ret_dict = {1: num1}
        for i in range(2, 10):
            ret_dict[i] = self.add(num1, ret_dict[i-1])
        ret = []
        base = 0
        for i in range(0, len2):
            times = int(num2[len2-i-1])
            if times != 0:
                temp = ret_dict[times]
                for j in range(0, base):
                    temp += "0"
                ret.append(temp)
            base += 1
        return functools.reduce(self.add, ret)





    def add(self, num1, num2):
        len1 = len(num1)
        len2 = len(num2)
        if len1 < len2 or (len1 == len2 and num1 < num2):
            num1, num2 = num2, num1
            len1, len2 = len2, len1
        extral_v = 0
        ans = ""
        for i in range(0, len2):
            value = int(num1[len1-i-1]) + int(num2[len2-i-1]) + extral_v
            v = value % 10
            extral_v = value // 10
            ans = str(v) + ans

        for i in range(len2, len1):
            value = int(num1[len1-i-1]) + extral_v
            v = value % 10
            extral_v = value // 10
            ans = str(v) + ans
        if extral_v > 0:
            ans = str(extral_v) + ans
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.add("99", "1"), 99+1)
    print(s.add("99", "100"), 99+100)
    print(s.add("99", "102"), 99+102)
    print(s.add("99", "11"), 99+11)

    print("----------------------")
    print(s.multiply("2", "3"), 2*3)
    print(s.multiply("2", "30"), 2*30)
    print(s.multiply("2", "31"), 2*31)
    print(s.multiply("21", "31"), 21*31)
    print(s.multiply("21", "0"), 21*0)
    print(s.multiply("21", "9"), 21*9)





